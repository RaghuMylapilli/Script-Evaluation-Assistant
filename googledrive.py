import httplib2
import io

from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'LearnAPI'

store = Storage('token.json')
credentials = store.get()
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    credentials = tools.run_flow(flow, store)
drive_service = discovery.build('drive', 'v3', http=credentials.authorize(httplib2.Http()))

def upload_file(filename, filepath, mime):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath,
                            mimetype=mime)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return file.get('id')

def download_file(file_id, file_path):
    request = drive_service.files().get_media(fileId=file_id)
    file_stream = io.BytesIO()
    downloader = MediaIoBaseDownload(file_stream, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    with io.open(file_path, 'wb') as file:
        file_stream.seek(0)
        file_data = file_stream.read()
        file.write(file_data)

def list_files():
    pass
