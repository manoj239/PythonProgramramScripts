import boto3

REGION = input("Please enter the Region: ")
print(type(REGION))


aws_access_key = "AKIAWOAVSQWULBVSVU5Q"
aws_secret_key = "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"
aws_region = "ap-south-1"

client = boto3.client('ec2',region_name=REGION)
vpc_list = client.describe_vpcs()
print(vpc_list)