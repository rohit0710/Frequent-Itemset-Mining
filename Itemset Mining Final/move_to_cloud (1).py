from Amazon import Amazon
import sys

REGION_HOST = 's3.ap-south-1.amazonaws.com'
AWS_ACCESS_KEY = 'AKIAJN4XZJ6UWPFU7ZSQ'
AWS_ACCESS_SECRET_KEY = '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'

if len(sys.argv) < 1:
    print "ERROR!!"
    print "Usage : python move_to_cloud.py <file>"
    sys.exit()

filename = sys.argv[1]
file = open(filename, 'r+')

key = file.name
bucket = 'hadoop-pro'

amazon = Amazon()
if amazon.upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key, host = REGION_HOST):
    print 'Uploaded data to cloud Successfully!'
else:
    print 'Uploading file to cloud failed...'

file.close()
