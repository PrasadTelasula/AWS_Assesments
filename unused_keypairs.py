import boto3
ec2 = boto3.client('ec2')
keys = ec2.describe_key_pairs()['KeyPairs']
instance = ec2.describe_instances()['Reservations']
for i in keys:
  key = i['KeyName']
#  for j in instance:
  ins = instance[0]['Instances'][0]['KeyName']	
  if key not in ins:
       print key
#for i in keys[0]['KeyName']:
#  for j in instance: 
#    if i not in j:
#	print i


