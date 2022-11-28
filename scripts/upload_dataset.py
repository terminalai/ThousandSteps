from google.cloud import storage
import sys

GCP_PROJECT_ID = "gait-analyzer-1ac2c"
BUCKET_NAME = "pdbiostamp-rc21"

client = storage.Client(
    project=GCP_PROJECT_ID,
)

def upload(zipfile_url):
    archive = open(zipfile_url, mode="rb")

    object_name = 'super-important-data-v1'
    bucket = client.bucket(BUCKET_NAME)

    blob = storage.Blob(object_name, bucket)
    blob.upload_from_file(archive, content_type='application/zip')

if __name__ == "__main__":
    for arg in sys.argv:
        if ".zip" in arg:
            print("Uploading", arg)
            upload(arg)
            print("Uploaded", arg)
            print()
