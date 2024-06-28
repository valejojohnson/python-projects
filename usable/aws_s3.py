# This python code is designed to take input from user on a bucket
# name to create. If bucket already exists, ask they'd like to delete it.
# Else, it will create the bucket and give feedback that it's been created.

import time
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
s3 = boto3.client('s3')
response = ''

def check_s3_bucket(bucket):
    try:
        s3.head_bucket(Bucket=bucket)
        print()
        print(f"S3 Bucket already exists: {bucket}")
        print()
        answer = input(f'Would you like to delete {bucket}? (Y/N) ')
        if answer == 'Y'.casefold():
            delete_s3_bucket(bucket)

    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"The bucket {bucket} DOESN'T already exist")
            print()
            print(f'creating bucket {bucket}..')
            create_s3_bucket(bucket)
        else:
            raise


def create_s3_bucket(bucket):
    try:
        s3.create_bucket(Bucket=bucket)
        print(f'Bucket {bucket} successfully created')
    except ClientError as e:
        print(f'There was an error creating the bucket: {e}')


def delete_s3_bucket(bucket):
    try:
        s3.delete_bucket(Bucket=bucket)
        print()
        print(f"S3 Bucket has been destroyed: {bucket} ")
        print()
    except ClientError as e:
        print(f"There was a problem deleting {bucket}: {e}")


def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    for name in bucket_names:
        print()
        print(name)


while response != False:
    response = input("Would you like to create a new bucket (Y/N) ")
    if response == 'Y'.casefold():
        print()
        bucket = input('Name the bucket to create?: ')
        check_s3_bucket(bucket)
    else:
        print()
        print('Exiting Program.')
        response = False


