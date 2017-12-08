import boto3
import sys
from colorama import *

def list_rds():
 client = boto3.client('rds')
 rds_ins = client.describe_db_instances()['DBInstances']
 print (Fore.MAGENTA + Style.BRIGHT + '\n===== Listing No MultiAZ RDS Instances =====')
 print Style.RESET_ALL
 print len(rds_ins)
 for i in rds_ins:
    if len(i) == '0':
        print "No RDS Instances found"

    elif len(i) != '0' and  i['MultiAZ'] == False:
        print (Fore.YELLOW + Style.BRIGHT + 'RDS EndPoint : ' + Fore.GREEN + Style.BRIGHT + i['Endpoint']['Address'] + Fore.YELLOW + Style.BRIGHT + '	MultiAZ : ' +  Fore.GREEN + Style.BRIGHT + str(i['MultiAZ']))
        print Style.RESET_ALL

def main():
    list_rds()

if __name__ == '__main__':
    sys.exit(main())

