import tkinter as tk
from tkinter import filedialog
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from tkinter import messagebox
import boto3
import os
import webbrowser
import dropbox
import requests
from boxsdk import OAuth2, Client

DROPBOX_ACCESS_TOKEN = 'Your_Drop_box_Access_Token'

SCOPES = ['https://www.googleapis.com/auth/drive.file']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    flow = InstalledAppFlow.from_client_secrets_file('path_to_your_credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

drive_service = build('drive', 'v3', credentials=creds)

selected_files = []

def classify_and_upload(file_path):
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
    file_type = os.path.splitext(file_path)[-1][1:].lower()  # Get file extension without dot
    
    video_formats = ['3gp', 'avi', 'flv', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'wmv']
    image_formats = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']

    uploaded_to = ""

    if file_size <= 2 and file_type in ['docx', 'txt', 'csv', 'xml']:
        upload_to_drive(file_path)
        uploaded_to = "Google Drive"
    elif file_type in video_formats:
        upload_to_pcloud(file_path)
        uploaded_to = "pCloud"
    elif file_size > 2 and file_type in ['txt', 'docx', 'csv', 'xml']:
        upload_to_dropbox(file_path)
        uploaded_to = "Dropbox"
    elif file_type in image_formats:
        upload_to_s3(file_path)
        uploaded_to = "Amazon S3"
    elif file_type in ['pdf', 'pptx']:
        upload_to_box(file_path)
        uploaded_to = "Box.com"
    else:
        print("File does not meet the criteria for uploading.")

    if uploaded_to:
        file_name = os.path.basename(file_path)
        file_size_formatted = format_size(get_file_size(file_path))
        message = f"The '{file_name}' of size {file_size_formatted} has been uploaded to {uploaded_to}."
        messagebox.showinfo("Upload Successful", message)
    else:
        print("File does not meet the criteria for uploading.")

def browse_files():
    global selected_files
    files = filedialog.askopenfilenames(title="Select Files", filetypes=(("All Files", "*.*"),))
    
    if len(files) > 0:
        selected_files = list(files)
        file_info.delete(1.0, tk.END)
        file_info.config(state=tk.NORMAL)
        
        for file_path in selected_files:
            file_name = os.path.basename(file_path)
            file_type = file_name.split(".")[-1].lower()
            file_size = format_size(get_file_size(file_path))
        
            classify_and_upload(file_path)
            file_info.insert(tk.END, f"{file_name} - {file_type.upper()} - {file_size}\n")
        file_info.config(state=tk.DISABLED)


def upload_to_pcloud(file_path):
    url = 'https://api.pcloud.com/uploadfile' 
    folder_id = 'your_pcloud_folder_id'
    access_token = 'your_pcloud_access_token'

    files = {'file': (file_path.split('/')[-1], open(file_path, 'rb'))}

    params = {
        'access_token': access_token,
        'folderid': folder_id,
    }

    response = requests.post(url, files=files, params=params)
    return response

def upload_files_to_pcloud():
    global selected_files
    if selected_files:
        uploaded_file_ids = []
        for file_path in selected_files:
            response = upload_to_pcloud(file_path)
            if response.status_code == 200:
                uploaded_file_ids.append(file_path)
                file_name = file_path.split('/')[-1]
                file_size = format_size(get_file_size(file_path))
                file_info.insert(tk.END, f"Uploaded: {file_name} - Size: {file_size}\n")
        show_upload_message(uploaded_file_ids, "pCloud")
    else:
        messagebox.showwarning("No Files Selected", "Please select files before uploading.")

def upload_to_s3(file_path):
   
    s3 = boto3.resource(
        service_name='s3',
        region_name='ap-south-1',
        aws_access_key_id='AWS_ACCESS_KEY_ID',
        aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
    )

    bucket_name = 'Bucket_Name'
    object_key = file_path.split('/')[-1]

    s3.Bucket(bucket_name).upload_file(Filename=file_path, Key=object_key)
    return object_key

def upload_files_to_s3():
    global selected_files
    if selected_files:
        uploaded_file_ids = []
        for file_path in selected_files:
            uploaded_file_id = upload_to_s3(file_path)
            uploaded_file_ids.append(uploaded_file_id)
            file_name = file_path.split('/')[-1]
            file_size = format_size(get_file_size(file_path))
            file_info.insert(tk.END, f"Uploaded: {file_name} - Size: {file_size} - File ID: {uploaded_file_id}\n")
        show_upload_message(uploaded_file_ids, "Amazon S3")
    else:
        messagebox.showwarning("No Files Selected", "Please select files before uploading.")


def upload_to_dropbox(file_path):
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    with open(file_path, 'rb') as f:
        file_content = f.read()
    file_name = os.path.basename(file_path)
    uploaded_file = dbx.files_upload(file_content, '/' + file_name)
    return uploaded_file.id

def upload_files_to_dropbox():
    global selected_files
    if selected_files:
        uploaded_file_ids = []
        for file_path in selected_files:
            uploaded_file_id = upload_to_dropbox(file_path)
            uploaded_file_ids.append(uploaded_file_id)
            file_name = os.path.basename(file_path)
            file_size = format_size(get_file_size(file_path))
            file_info.insert(tk.END, f"Uploaded: {file_name} - Size: {file_size} - File ID: {uploaded_file_id}\n")
        show_upload_message(uploaded_file_ids, "DropBox")
    else:
        messagebox.showwarning("No Files Selected", "Please select files before uploading.")

def upload_to_box(file_path):
    
    client_id = 'box.com_client_id'
    client_secret = 'box.com_client_secret'
    access_token = 'box.com_access_token'
    refresh_token = 'box.com_refresh_token'

    
    auth = OAuth2(client_id, client_secret, access_token=access_token, refresh_token=refresh_token)

    
    client = Client(auth)

    file_name = os.path.basename(file_path)
    folder_id = '222415341532' 
    folder = client.folder(folder_id).get()
    uploaded_file = folder.upload(file_path, file_name)
    return uploaded_file.id

def upload_files_to_box():
    global selected_files
    if selected_files:
        uploaded_file_ids = []
        for file_path in selected_files:
            uploaded_file_id = upload_to_box(file_path)
            uploaded_file_ids.append(uploaded_file_id)
            file_name = os.path.basename(file_path)
            file_size = format_size(get_file_size(file_path))
            file_info.insert(tk.END, f"Uploaded: {file_name} - Size: {file_size} - File ID: {uploaded_file_id}\n")
        show_upload_message(uploaded_file_ids, "Box.com")
    else:
        messagebox.showwarning("No Files Selected", "Please select files before uploading.")


DESTINATION_FOLDER_ID = 'Google_Drive_Folder-Id'

def upload_to_drive(file_path):
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [DESTINATION_FOLDER_ID]
    }
    media = MediaFileUpload(file_path, mimetype='application/octet-stream')
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    
    return uploaded_file.get('id')

def upload_files_to_drive():
    global selected_files
    if selected_files:
        uploaded_file_ids = []
        for file_path in selected_files:
            uploaded_file_id = upload_to_drive(file_path)
            uploaded_file_ids.append(uploaded_file_id)
            file_name = os.path.basename(file_path)
            file_size = format_size(get_file_size(file_path))
            file_info.insert(tk.END, f"Uploaded: {file_name} - Size: {file_size} - File ID: {uploaded_file_id}\n")
        show_upload_message(uploaded_file_ids, "Google Drive")
    else:
        messagebox.showwarning("No Files Selected", "Please select files before uploading.")

def show_upload_message(file_ids, destination):
    uploaded_file_info = []
    for file_id, file_path in zip(file_ids, selected_files):
        file_name = os.path.basename(file_path)
        file_size = format_size(get_file_size(file_path))
        uploaded_file_info.append(f"The '{file_name}' of size {file_size} has been uploaded to {destination}. File ID: {file_id}")
    
    message = "\n".join(uploaded_file_info)
    messagebox.showinfo("Upload Complete", message)


def get_file_size(file_path):
    return os.path.getsize(file_path) / (1024 * 1024)

def format_size(size):
    if size < 1:
        return f"{size:.2f} KB"
    else:
        return f"{size:.2f} MB"

def open_github_profile(event):
    webbrowser.open_new("https://github.com/alok-2002")


root = tk.Tk()  
root.title("PyCloudFlow")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

root.configure(bg="#2C3E50")
root.iconbitmap('./assets/Logo.ico')

heading_font = ("Garamond", 36, "bold italic")
heading_label = tk.Label(root, text="PyCloudFlow", font=heading_font, bg="#2C3E50",fg="#ECF0F1")
heading_label.pack(pady=20)

button_font = ("Arial", 18)
button_bg = "#3498DB" 
button_fg = "#FFFFFF"

text_font = ("Helvetica", 12)
text_bg = "#34495E" 
text_fg = "#ECF0F1"

browse_button = tk.Button(root, text="Browse Files", command=browse_files, font=button_font,bg=button_bg, fg=button_fg)
browse_button.pack(pady=10)

# upload_button = tk.Button(root, text="Upload To Google Drive", command=upload_files_to_drive, font=button_font,bg=button_bg, fg=button_fg)
# upload_button.place(x=100, y=650)

# upload_dropbox_button = tk.Button(root, text="Upload To Dropbox", command=upload_files_to_dropbox, font=button_font,bg=button_bg, fg=button_fg)
# upload_dropbox_button.place(x=400, y=650)

# upload_box_button = tk.Button(root, text="Upload To Box.com", command=upload_files_to_box, font=button_font,bg=button_bg, fg=button_fg)
# upload_box_button.place(x=650, y=650)

# upload_pcloud_button = tk.Button(root, text="Upload To pCloud", command=upload_files_to_pcloud, font=button_font, bg=button_bg, fg=button_fg)
# upload_pcloud_button.place(x=920, y=650)

# upload_s3_button = tk.Button(root, text="Upload to S3", command=upload_files_to_s3, font=button_font, bg=button_bg, fg=button_fg)
# upload_s3_button.place(x=1150, y=650)

copyright_button = tk.Button(root, text="Copyright © Alok Shamra", font=text_font, borderwidth=0, command=open_github_profile, bg=text_bg, fg=text_fg, cursor="hand2")
copyright_button.pack(side="bottom", anchor="se")

file_info = tk.Text(root, height=20, width=80, font=text_font,bg=text_bg, fg=text_fg)
file_info.pack()

root.mainloop()
