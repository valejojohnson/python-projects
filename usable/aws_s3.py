# This python code is designed to take input from user on a bucket
# name to create. If bucket already exists, ask they'd like to delete it.
# Else, it will create the bucket and give feedback that it's been created.

import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)  # This is to constantly reset the color after every run
region = 'us-east-1'
s3 = boto3.client('s3', region_name=region)  # Don't feel like typing out boto.client('s3') everytime


def check_items__in_bucket(bucket):
    if s3.list_objects_v2(Bucket=bucket) != '':
        return True  # Meaning bucket isn't empty
    else:
        return False


def check_s3_bucket(bucket):
    try:
        if s3.head_bucket(Bucket=bucket):
            check_items__in_bucket(bucket)
            if check_items__in_bucket(bucket) is True:
                print(Fore.YELLOW + f"S3 Bucket already exists but it's not empty: {bucket}")
            else:
                print(Fore.YELLOW + f"S3 Bucket already exists but it's empty: {bucket}")
        print()
        answer = input(f'Would you like to delete {bucket}? (Y/N) ').strip().lower()
        if answer == 'y':
            delete_s3_bucket(bucket)

    except ClientError as e:
        if e.response['Error']['Code'] == '404':

            print(Fore.YELLOW + f"The bucket {bucket} DOESN'T exist.")
            print()
            create_s3_bucket(bucket)
        else:
            raise


def create_s3_bucket(bucket, region):
    try:
        if region is None or region == 'us-east-1':
            location = {'LocationConstraint': 'us-east-1'}
            print(f'Creating bucket in US-EAST-1: {bucket}')
            s3.create_bucket(Bucket=bucket, CreateBucketConfiguration=location)
            print(Fore.GREEN + f'Bucket {bucket} successfully created')
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket, CreateBucketConfiguration=location)
            print(Fore.GREEN + f'Bucket {bucket} successfully created in {region}')
        question = input('Would you like to list all buckets? (Y/N)').strip().lower()
        if question == 'y':
            list_s3_buckets()
    except ClientError as e:
        print(Fore.RED + f'There was an error creating the bucket: {e}')


def delete_s3_bucket(bucket):
    try:
        s3.delete_bucket(Bucket=bucket)
        print()
        print(f"S3 Bucket has been destroyed: {bucket} ")
        print()
    except ClientError as e:
        print(Fore.RED + f"There was a problem destroying {bucket}: {e}")


def list_s3_buckets():
    # List all S3 buckets.
    try:
        response = s3.list_buckets()
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        print("Buckets:")
        for name in bucket_names:
            print(name)
    except ClientError as e:
        print(Fore.RED + f"Error listing buckets: {e}")


def check_credentials(bucket):
    try:
        s3.list_buckets()
        print(Fore.GREEN + "AWS credentials valid. Moving on")
        print()
        check_s3_bucket(bucket)
    except NoCredentialsError:
        print()
        print(Fore.RED + "No credentials were found")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'AccessDenied':
            print(Fore.RED + "Access is denied. Check your credentials")
        else:
            print(Fore.RED + f"An error occurred: {e}")


def main(region):
    while True:

        print()
        response = input("Would you like to check/create a new bucket (Y/N) ").strip().lower()
        if response == 'y':
            print()
            bucket = input('Name the bucket to check/create?: ').strip().lower()
            check_credentials(bucket, region)
        elif response == 'n':
            print(Fore.RED + 'Exiting Program')
            return False
        else:
            print()
            print(Fore.YELLOW + "Invalid input. Please enter 'Y' or 'N'. ")


if __name__ == '__main__':
    main(region)
