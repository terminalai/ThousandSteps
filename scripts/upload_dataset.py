from google.cloud import storage
import sys

client = storage.Client(
    project="gait-analyzer-1ac2c",
)

def upload(zipfile_url):
    archive = open(zipfile_url, mode="rb")

    object_name = 'super-important-data-v1'
    bucket = client.bucket("pdbiostamp-rc21")

    blob = storage.Blob(object_name, bucket)
    blob.upload_from_file(archive, content_type='application/zip')

if __name__ == "__main__":
    for arg in sys.argv:
        if ".zip" in arg:
            print("Uploading", arg)
            upload(arg)
            print("Uploaded", arg)
            print()
