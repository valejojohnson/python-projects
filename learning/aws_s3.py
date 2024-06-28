import time
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError


def check_s3_bucket(bucket):
    try:
        s3.head_bucket(Bucket=bucket)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"The bucket {bucket} DOESN'T exist in this account")
            print()
            print(f'creating bucket {bucket}..')
            print()
            return False
        else:
            raise


def create_s3_bucket(bucket):
    try:
        s3.create_bucket(Bucket=bucket)
        print(f'Bucket {bucket} successfully created')
        return True
    except ClientError as e:
        print(f'There was an error creating the bucket: {e}')
        return False


def delete_s3_bucket(bucket):
    try:
        s3.delete_bucket(Bucket=bucket)
        print()
        print(f"Bucket {bucket} has been removed.")
    except ClientError as e:
        print(f"There was a problem deleting {bucket}: {e}")
        return False


def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    for name in bucket_names:
        print()
        print(name)


s3 = boto3.client('s3')
bucket = input('Which bucket would you like to check?: ')
if not check_s3_bucket(bucket):
    create_s3_bucket(bucket)
    print('Listing Existing Buckets: ')
    list_s3_buckets()
    time.sleep(10)
    print(f"Deleting bucket {bucket}")
    delete_s3_bucket(bucket)
else:
    print(f"Bucket {bucket} already present")

