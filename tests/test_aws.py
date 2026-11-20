
import os

import boto3
from dotenv import load_dotenv
from botocore.exceptions import BotoCoreError, ClientError

load_dotenv()

# Load IAM credentials from .env
access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION", "ap-south-1")

if not access_key or not secret_key:
    raise ValueError("AWS credentials missing from .env")

# Create authenticated AWS session
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region,
)

def test_aws():
    try:
        sts = session.client("sts")
        response = sts.get_caller_identity()

        print("✅ AWS authentication successful")
        print(f"Account: {response['Account']}")
        print(f"IAM ARN: {response['Arn']}")
    except (ClientError, BotoCoreError) as e:
        print(f"❌ AWS authentication failed: {e}")

def test_s3():
    try:
        s3 = session.client("s3")
        response = s3.list_buckets()

        print("✅ S3 API access successful")
        print("Buckets:")
        for bucket in response["Buckets"]:
            print(f"  - {bucket['Name']}")
    except (ClientError, BotoCoreError) as e:
        print(f"❌ S3 access failed: {e}")

def test_ec2():
    try:
        ec2 = session.client("ec2")
        response = ec2.describe_instances()

        instances = [
            instance["InstanceId"]
            for reservation in response["Reservations"]
            for instance in reservation["Instances"]
        ]

        print("✅ EC2 API access successful")
        print(f"Region: {region}")
        print(f"Instances: {instances}")
    except (ClientError, BotoCoreError) as e:
        print(f"❌ EC2 access failed: {e}")

if __name__ == "__main__":
    test_aws()
    test_s3()
    test_ec2()
