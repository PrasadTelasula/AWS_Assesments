import boto3
from datetime import datetime, timedelta
from prettytable import PrettyTable


ptable = PrettyTable(["Snapshot Identifier", "Snapshot Created Date",  "Instance Identifier", "RDS Instance Created Date"])


N = 60
date_N_days_ago = datetime.now() - timedelta(days=N)
date_2_months_ago = date_N_days_ago.strftime("%Y-%m-%d")


client = boto3.client('rds')
snaps = client.describe_db_snapshots()['DBSnapshots']


for i in snaps:
  Instance_identifier = i['DBInstanceIdentifier']
  snap_id_dates = i['SnapshotCreateTime'].strftime("%Y-%m-%d")
  instance_create_date = i['InstanceCreateTime'].strftime("%Y-%m-%d")
  snap_identifier = i['DBSnapshotIdentifier']

  if snap_id_dates <= date_2_months_ago:
     ptable.add_row([snap_identifier,snap_id_dates,Instance_identifier,instance_create_date])



print ptable
