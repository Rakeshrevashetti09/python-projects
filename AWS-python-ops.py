import boto3
s3 =boto3.resource('s3')
ec2=boto3.resource('ec2')

for bucket in s3.buckets.all():
    print(bucket.name)
    print(s3.buckets(all))

s3.Bucket("trainwithshubham").download_file("thumbnail.png")