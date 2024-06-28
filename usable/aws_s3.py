# This python code is designed to take input from user on a bucket
# name to create. If bucket already exists, ask they'd like to keep it.
# Else, it will create the bucket.

import time
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
s3 = boto3.client('s3')


def check_s3_bucket(bucket):
    try:
        s3.head_bucket(Bucket=bucket)
        print()
        print(f"S3 Bucket already exists: {bucket}")
        print()
        answer = input(f'Would you like to delete {bucket}? (Y/N)')
        if answer == 'Y':
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
        print(f"Bucket {bucket} has been destroyed.")
    except ClientError as e:
        print(f"There was a problem deleting {bucket}: {e}")


def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    for name in bucket_names:
        print()
        print(name)


bucket = input('Which bucket would you like to create?: ')
check_s3_bucket(bucket)
