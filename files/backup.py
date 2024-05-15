from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Initialize Google authentication and create the Google Drive instance
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# List of files to be uploaded with their IDs, filenames, and full paths
upload_file_list = [
    {
        'filename': 'wordpress.sql',
        'path': '{{ global_backup_db }}/wordpress.sql',  # Full local path
        'id': '1Sg1-lDb2mFwGpq6-xfi_T38NK3gtONn5'
    },
    {
        'filename': 'wp-frontend.zip',
        'path': '{{ global_backup_site }}/wp-frontend.zip',  # Full local path
        'id': '10yBJv6NYuo5uZqLiKTRhXen6pPtTAAfU'
    }
]

# Loop through the file list and upload each file
for upload_file in upload_file_list:
    # Create a Google Drive file instance with the specified parent folder and file ID
    gfile = drive.CreateFile({
        'parents': [{'id': '1kNQlqkQrgYPfLpmhI7uPq0OQiSlyfsQR'}],
        'id': upload_file['id']
    })

    # Set the content of the file from the local filename
    gfile.SetContentFile(upload_file['filename'])

    # Upload the file to Google Drive
    gfile.Upload()
    # Optional: print out the title and ID of the uploaded file (uncomment to use)
    # print('title: %s, id: %s' % (gfile['title'], gfile['id']))
