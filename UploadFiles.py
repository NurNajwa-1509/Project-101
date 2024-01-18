import dropbox
from dropbox.files import WriteMode
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.BosyJplv4MWZwJL64jH6w042YKaBPMEHr8XZ3W5SrtQaWW3k4VqyxaQncwlJiLbS9hmPOhXa8PIgzvZewg4qpmQNATlpM4QMYTjtx-QoeFeOb6B-aSfFcJMque7u2qvSA5SRfqGpfH8R'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 

    transferData.upload_file(file_from, file_to)
    print("File has been Uploaded !!!")

main()
