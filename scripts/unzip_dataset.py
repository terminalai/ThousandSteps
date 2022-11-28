from google.cloud import storage
from zipfile import ZipFile
from zipfile import is_zipfile
import io

GCP_PROJECT_ID = "gait-analyzer-1ac2c"
BUCKET_NAME = "pdbiostamp-rc21"

client = storage.Client(
    project=GCP_PROJECT_ID,
)

def zipextract(bucketname, zipfilename_with_path):
    bucket = client.bucket(bucketname)
    
    destination_blob_pathname = zipfilename_with_path
    blob = bucket.blob(destination_blob_pathname)
    zipbytes = io.BytesIO(blob.download_as_string())

    if is_zipfile(zipbytes):
        with ZipFile(zipbytes, 'r') as myzip:
            for contentfilename in myzip.namelist():
                contentfile = myzip.read(contentfilename)
                blob = bucket.blob(zipfilename_with_path + "/" + contentfilename)
                blob.upload_from_string(contentfile)

if __name__ == "__main__":
    for arg in sys.argv:
        if ".zip" in arg:
            print("Uploading", arg)
            upload(arg)
            print("Uploaded", arg)
            print()


zipextract(BUCKET_NAME, "super-important-data-v1") # if the file is gs://mybucket/path/file.zip
