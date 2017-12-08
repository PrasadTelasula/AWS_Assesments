import boto3
import sys
from prettytable import PrettyTable

ptable = PrettyTable(["SecurityGroup Name","No.. OF Inbound Rules"])

N = 3 #Change according to required Security Group Inbound count

def list_sg_inbound_rules_count():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()['SecurityGroups']
    for i in response:
      sg = i['GroupName']
      if sg != 'default' and len(i['IpPermissions']) >= N:
    	 ptable.add_row([i['GroupName'],len(i['IpPermissions'])])
    print "\n", ptable, "\n"


def main():
    list_sg_inbound_rules_count()

if __name__ == '__main__':
    sys.exit(main())

      
