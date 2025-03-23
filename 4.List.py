import boto3
from dotenv import  load_dotenv
import os
ENV_FILE = '.env_dev'
load_dotenv(ENV_FILE)
# Check if the environment variable is loaded
print(os.getenv('AWS_DEFAULT_REGION'))
#ec2_client = boto3.client('ec2',region_name=os.getenv('AWS_DEFAULT_REGION'))
ec2_client = boto3.client('ec2',region_name='ap-south-1')
#print(ec2_client.describe_regions())
regions_list = []
for region in ec2_client.describe_regions().get('Regions'):
    regions_list.append(region.get('RegionName'))
print(regions_list)

#Using list comphrension

comp_list= [ region['RegionName'] for region in ec2_client.describe_regions().get
('Regions')]