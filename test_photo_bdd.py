from werkzeug.utils import secure_filename
from PIL import Image
import boto3
s3 = boto3.client('s3',
                    aws_access_key_id='AKIAVA5FQS275KLPM7ND',
                    aws_secret_access_key= '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',
                     )
BUCKET_NAME='myphotobucketraph'
img = Image.open('/Users/raphaeldiaz/Desktop/ruedelafoi.jpg')
if img:
    filename = secure_filename(img.filename)
    img.save(filename)
    s3.upload_file(
        Bucket = BUCKET_NAME,
        Filename=filename,
        Key = filename
    )
    
    msg = "Upload Done ! "
    print(msg)


    