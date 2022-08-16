from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from matplotlib import image
from PIL import Image
import boto3
s3 = boto3.client('s3',
                    aws_access_key_id='AKIAVA5FQS27ZQZRC4ER',
                    aws_secret_access_key= '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',
                     )
BUCKET_NAME='myphotobucketraph'
img = Image.open('/Users/raphaeldiaz/Desktop/image4.jpg')
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