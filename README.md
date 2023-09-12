# Python Cloud Flow

 ![GitHub](https://img.shields.io/github/license/alok-2002/PythonCloudFlow)
 ![GitHub stars](https://img.shields.io/github/stars/alok-2002/PythonCloudFlow)
 ![GitHub forks](https://img.shields.io/github/forks/alok-2002/PythonCloudFlow)
 ![GitHub repo size](https://img.shields.io/github/repo-size/alok-2002/PythonCloudFlow)


Py_Cloud_Flow is a versatile Python script that empowers users to seamlessly upload files to various cloud storage services, including `Google Drive`, `Dropbox`, `Box.com`, `pCloud`, and `Amazon S3`. The script offers a modern graphical user interface (GUI) built using the `tkinter` library, making it convenient and user-friendly for both beginners and experienced users.


## PyCloudFlow 
![Screenshot 2023-08-23 151919](https://github.com/Alok-2002/PythonCloudFlow/assets/93814546/a11e9cea-b8b3-4316-b7b6-b1d8d0d1ee1d)


## PyCloudFlow Automated
![Automated](https://github.com/Alok-2002/PythonCloudFlow/assets/93814546/5d506e49-c057-4640-8ddc-e9f2c87cb6e8)


## Features

- **Fully Automatic:** Python_Cloud_Flow is now a fully automatic application. Users only need to select files, and the program automatically applies file classification and uploads the files to the appropriate cloud service.
- **Multi-Cloud Support:** Upload files to a variety of popular cloud storage platforms from a single interface.
- **Interactive GUI:** The script offers an interactive GUI that simplifies the process of selecting and uploading files.
- **Real-Time Feedback:** Monitor the upload progress and receive instant feedback on uploaded file details.
- **Effortless Setup:** A well-organized structure and clear configuration instructions facilitate seamless setup and usage.

## Prerequisites

Before using Python_Cloud_Flow, ensure that you have the following prerequisites:

- **Python 3.x:** Make sure you have a Python interpreter installed on your machine.
- **Required Libraries:** Install the necessary Python libraries using the following command:

   ```
   pip install google-api-python-client boto3 dropbox requests boxsdk tkinter
   ```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Alok-2002/Python_Cloud_Flow.git
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
   - The automatic classification process will determine the appropriate cloud service based on the file's characteristics.
   - The upload process will be initiated automatically based on the classification.
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

Contributions to this project are highly encouraged. If you encounter issues, have suggestions, or want to add new features, [please open an issue](https://github.com/Alok-2002/PythonCloudFlow/issues/new) or submit a pull request.

## Copyright
This project is the original work of [Alok Sharma](https://github.com/Alok-2002) If you use or modify this project, you are required to give proper credit by providing a link to the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
