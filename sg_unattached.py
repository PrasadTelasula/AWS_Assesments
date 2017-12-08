import boto3

ec2 = boto3.client('ec2')
instance = ec2.describe_instances()['Reservations']
sg = ec2.describe_security_groups()['SecurityGroups']

for i in sg:
   sg_name = i['GroupName']
   if instance[0]['Instances'][0]['State']['Name'] != 'terminated':
     ins = instance[0]['Instances'][0]['SecurityGroups'][0]['GroupName']
     if sg_name not in ins:
          print sg_name
#for i in keys
 
#print instance[0]['Instances'][0]['State']['Name']
#print instance[0]['Instances'][0]['SecurityGroups'][0]['GroupName']
