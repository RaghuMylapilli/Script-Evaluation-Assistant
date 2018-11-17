from __future__ import print_function
import httplib2
import os
import Auth

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'LearnAPI'

auth = Auth.Authorisation(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
credentials = auth.getCredentials()
service = discovery.build('drive', 'v3', http=credentials.authorize(httplib2.Http()))

def upload_files(filename, filepath, mime):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath,
                            mimetype=mime)
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print ('File ID: %s' % file.get('id'))

upload_files('JMJ.jpg', 'JMJ.jpg', 'image/jpeg')

upload_files('JMJ.jpg', 'JMJ.jpg', 'image/jpeg')