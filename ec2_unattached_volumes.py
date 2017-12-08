import boto3
import sys

def list_unattached_volumes():
    client = boto3.client('ec2')
    conn = boto3.resource('ec2')
    #volumes = conn.volumes.all()
    volumes = conn.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])
    for i in volumes: 
	print i



def main():
    list_unattached_volumes()

if __name__ == '__main__':
    sys.exit(main())
