import boto3
from colorama import *
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
       for i in instance["BlockDeviceMappings"]:
        # This sample print will output entire Dictionary object
          if i['Ebs']['DeleteOnTermination'] == False :
                print "\n"
		print Fore.MAGENTA + Style.BRIGHT + 'InstanceID : ' + Fore.GREEN + Style.BRIGHT + instance['InstanceId'] + Fore.MAGENTA + Style.BRIGHT + '	VolumeID : ' + Fore.GREEN + Style.BRIGHT + i['Ebs']['VolumeId'] + Fore.MAGENTA + Style.BRIGHT + '	Delete On Terminstion : ' + Fore.GREEN + Style.BRIGHT + str( i['Ebs']['DeleteOnTermination'])
		print Style.RESET_ALL
