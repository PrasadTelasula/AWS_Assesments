import boto3
import sys
from colorama import *

def list_nosnap_volumes():
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')
    volumes = ec2.volumes.all()
    snaps = client.describe_snapshots(OwnerIds=['self'])['Snapshots']
    print (Fore.MAGENTA + Style.BRIGHT + '\n===== Listing No Snapshot Volumes =====\n')
    print Style.RESET_ALL
    for v in volumes:
  
      if len(snaps) == 0:
         print  (Fore.YELLOW + Style.BRIGHT + 'No Snapshot found for VolumeID - ' +  Fore.GREEN + Style.BRIGHT + v.id )
         print Style.RESET_ALL
      elif len(snaps) != 0 and v.id not in snaps[0]['VolumeId'] :
         print  (Fore.YELLOW + Style.BRIGHT + 'No Snapshot found for VolumeID - ' +  Fore.GREEN + Style.BRIGHT + v.id )
         print Style.RESET_ALL


def main():
    list_nosnap_volumes()

if __name__ == '__main__':
    sys.exit(main())
