import boto3
from datetime import datetime, timedelta

N = 60
date_N_days_ago = datetime.now() - timedelta(days=N)
date_2_months_ago = date_N_days_ago.strftime("%Y-%m-%d")

#print datetime.now()
#print date_N_days_ago





ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
volumes = ec2.volumes.all()
snaps = client.describe_snapshots(OwnerIds=['self'])['Snapshots']

for i in snaps:
  #print i['SnapshotId']
  snap_ids = i['SnapshotId']
  #print i['StartTime'].strftime("%Y-%m-%d")
  snap_id_dates = i['StartTime'].strftime("%Y-%m-%d")
  if snap_id_dates <= date_2_months_ago:
    print i['SnapshotId'],i['StartTime']
#print snaps[0]['VolumeId'],snaps[0]['StartTime']

#date = snaps[0]['StartTime']
#print date.strftime("%Y-%m-%d")
