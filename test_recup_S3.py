

import boto3

s3 = boto3.client('s3',
                    aws_access_key_id='AKIAVA5FQS276OPE5LYU',
                    aws_secret_access_key= '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',
                     )
BUCKET_NAME='myphotobucketraph'
theobjects = s3.list_objects_v2(Bucket=BUCKET_NAME)
liste = []
for object in theobjects['Contents']:
    liste.append(object['Key'])
    #print (object['Key'])
nom_rue =[]
for i in range (len(liste)):
    
    x = liste[i].split('_',3)
    x = x[3].split('.',1)
    nom_rue.append(x[0])

for j in range(len(nom_rue)):
    print(nom_rue[j])


    
   
