# Usage Instructions
#    $ bash load_dataset.sh my_bucket_name directory_to_store_in
MY_BUCKET=$1
mkdir $2
gcsfuse --implicit-dirs --rename-dir-limit=100 --disable-http2 --max-conns-per-host=100 $MY_BUCKET $2

