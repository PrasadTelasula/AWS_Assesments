import boto3
import sys
import argparse


def list_rds():
 client = boto3.client('rds')
 rds_ins = client.describe_db_instances()['DBInstances']
 snaps = client.describe_db_snapshots()['DBSnapshots']
 for i in rds_ins:
   print i
   if i['DBInstanceStatus'] == 'available' and   i['DBInstanceIdentifier'] not in snaps[0]['DBInstanceIdentifier']:
     print i['Endpoint']['Address']
   elif len(i) == 0:
     print "No RDS Instances Found"

def main():
    list_rds()

if __name__ == '__main__':
    sys.exit(main())

#for i in rds_ins['DBInstances'][0]['Endpoint']['Address']:
# if  rds_ins['DBInstances'][0]['MultiAZ'] == True:
#  print rds_ins['DBInstances'][0]['MultiAZ'],rds_ins['DBInstances'][0]['Endpoint']['Address']
