import boto3
from colorama import *

s3 = boto3.resource('s3')
print (Fore.YELLOW + Style.BRIGHT + '\n===== Listing Public Access Buckets =====\n')
print Style.RESET_ALL
for bucket in s3.buckets.all():
#    print(bucket.name)
    acl = bucket.Acl()
    for grant in acl.grants:
       if grant['Grantee']['Type'].lower() == 'group'  and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':

          	 #print Fore.MAGENTA + Style.BRIGHT  + 'Bucket Name:', Fore.GREEN + Style.BRIGHT + bucket.name
                 #print Style.RESET_ALL
          
                 grant_permission = grant['Permission'].lower()
        	 if grant_permission == 'read':
			
          	 	print Fore.MAGENTA + Style.BRIGHT  + 'Bucket Name:', Fore.GREEN + Style.BRIGHT + bucket.name
               	        print(Fore.RED + Style.BRIGHT + 'Read - Public Access: List Objects')
                 	print Style.RESET_ALL

		 elif grant_permission == 'write':

          	 	print Fore.MAGENTA + Style.BRIGHT  + 'Bucket Name:', Fore.GREEN + Style.BRIGHT + bucket.name
			print(Fore.RED + Style.BRIGHT + 'Write - Public Access: Write Objects')
                 	print Style.RESET_ALL

		 elif grant_permission == 'read_acp':

			print Fore.MAGENTA + Style.BRIGHT  + 'Bucket Name:', Fore.GREEN + Style.BRIGHT + bucket.name
			print(Fore.RED + Style.BRIGHT + 'Write - Public Access: Read Bucket Permissions')
                 	print Style.RESET_ALL

		 elif grant_permission == 'write_acp':

	     		print Fore.MAGENTA + Style.BRIGHT  + 'Bucket Name:', Fore.GREEN + Style.BRIGHT + bucket.name
 			print(Fore.RED + Style.BRIGHT + 'Write - Public Access: Write Bucket Permissions')
                 	print Style.RESET_ALL

		 elif grant_permission == 'full_control':

          	        print Fore.MAGENTA + Style.BRIGHT  + 'Bucket Name:', Fore.GREEN + Style.BRIGHT + bucket.name
		        print(Fore.RED + Style.BRIGHT + 'Public Access: Full Control')
                 	print Style.RESET_ALL
