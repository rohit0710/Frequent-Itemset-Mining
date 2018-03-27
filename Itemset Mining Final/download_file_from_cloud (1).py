from Amazon import Amazon
import sys

REGION_HOST = 's3.ap-south-1.amazonaws.com'
AWS_ACCESS_KEY = 'AKIAJN4XZJ6UWPFU7ZSQ'
AWS_ACCESS_SECRET_KEY = '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'

if len(sys.argv) < 1:
    print "ERROR!!"
    print "Usage : python download_file_from_cloud.py <file>"
    sys.exit()

filename = sys.argv[1]

key = file.name
bucket = 'hadoop-pro'

amazon = Amazon()
if amazon.download_from_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, bucket, key, host = REGION_HOST, FILE_NAME = filename, LOCAL_PATH = "./"):
    print 'Downloaded file from cloud Successfully!'
else:
    print 'Downloading file from cloud failed...'
