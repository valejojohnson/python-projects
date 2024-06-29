# This python code is designed to take input from user on a bucket
# name to create. If bucket already exists, ask they'd like to delete it.
# Else, it will create the bucket and give feedback that it's been created.

import time
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from colorama import Fore, Style, init

# Constant Variables
init(autoreset=True)  # This is to constantly reset the color after every run
s3 = boto3.client('s3')  # Don't feel like typing out boto.client('s3') everytime
response = True  # This is to run the program until it's False


def check_s3_bucket(bucket):
    try:
        s3.head_bucket(Bucket=bucket)
        print()
        print(Fore.YELLOW + f"S3 Bucket already exists: {bucket}")
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
        question = input('Would you like to list all buckets? (Y/N)')
        if question == 'Y'.casefold():
            list_s3_buckets()
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
    listing = s3.list_buckets()

    bucket_names = [bucket['Name'] for bucket in listing['Buckets']]
    for name in bucket_names:
        print()
        print(name)


def check_credentials(bucket):
    try:
        s3.list_buckets()
        print(Fore.GREEN + "AWS credentials valid. Moving on")
        print()
        check_s3_bucket(bucket)
    except NoCredentialsError:
        print()
        print("No credentials were found")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'AccessDenied':
            print(f"Access is denied. Check credentials")
        else:
            print(f"An error occurred: {e}")


while response != False:
    print()
    response = input("Would you like to create a new bucket (Y/N) ")
    if response == 'y'.lower() or response == 'Y':
        print()
        bucket = input('Name the bucket to create?: ')
        check_credentials(bucket)
    else:
        print()
        print(Fore.RED + 'Exiting Program.')
        response = False


