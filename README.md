
# Python_Cloud_Flow

Python_Cloud_Flow is a versatile Python script that empowers users to seamlessly upload files to various cloud storage services, including Google Drive, Dropbox, Box.com, pCloud, and Amazon S3. The script offers a modern graphical user interface (GUI) built using the `tkinter` library, making it convenient and user-friendly for both beginners and experienced users.

## PyCloudFlow ScreenShots
![image](https://github.com/Alok-2002/PythonCloudFlow/assets/93814546/05ca5b34-e653-4e7b-8fbd-f67581fd77f2)



## Features

- **Multi-Cloud Support:** Upload files to a variety of popular cloud storage platforms from a single interface.
- **Interactive GUI:** The script offers an interactive GUI that simplifies the process of selecting and uploading files.
- **Real-Time Feedback:** Monitor the upload progress and receive instant feedback on uploaded file details.
- **Effortless Setup:** A well-organized structure and clear configuration instructions facilitate seamless setup and usage.

## Prerequisites

Before using Python_Cloud_Flow, ensure that you have the following prerequisites:

- **Python 3.x:** Make sure you have a Python interpreter installed on your machine.
- **Required Libraries:** Install the necessary Python libraries using the following command:

   ```
   pip install google-api-python-client boto3 dropbox requests boxsdk tk
   ```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/alok-2002/Python_Cloud_Flow.git
   cd Python_Cloud_Flow
   ```

2. **Configure Credentials:**

   Replace placeholders in the script with your API keys, tokens, and folder IDs. Refer to comments in the script for guidance on where to make these replacements.

3. **Run the Script:**

   ```bash
   python PyCloudFlow.py
   ```

4. **Using the GUI:**

   - Browse and select files for upload.
   - Choose the desired cloud service.
   - Click the corresponding "Upload" button to initiate the upload process.
   - Monitor the GUI for real-time feedback on uploaded files.

## Advanced Configuration

- **Customization:** Modify the script's appearance, add more cloud services, or enhance error handling to tailor it to your needs.
- **Enhanced Security:** Store your sensitive information, such as API keys and tokens, in environment variables for added security.
- **Automate Tasks:** Integrate the script with automation tools like `cron` or Windows Task Scheduler for scheduled uploads.

## Troubleshooting

- **API Quotas:** Ensure that your cloud service accounts have sufficient API quotas to accommodate uploads.
- **Dependencies:** Verify that all required libraries are installed using the correct version of Python.
- **API Keys and Tokens:** Double-check the accuracy of your API keys, tokens, and other credentials.

## Contributions

Contributions to this project are highly encouraged. If you encounter issues, have suggestions, or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

