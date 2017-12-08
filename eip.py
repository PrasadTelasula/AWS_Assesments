import boto3
import sys

def list_eip():
   client = boto3.client('ec2')
   addresses_dict = client.describe_addresses()
   for eip_dict in addresses_dict['Addresses']:
	if "NetworkInterfaceId" not in eip_dict:
	    print(eip_dict['PublicIp'])

def main():
    list_eip()

if __name__ == '__main__':
    sys.exit(main())
