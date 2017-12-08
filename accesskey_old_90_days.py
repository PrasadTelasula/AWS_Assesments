import boto3
from datetime import datetime, timedelta

N = 90
date_N_days_ago = datetime.now() - timedelta(days=N)
date_N_days_ago = datetime.utcnow() - timedelta(days=N)
date_90_days_ago = date_N_days_ago.strftime("%Y-%m-%d")


#print datetime.now().strftime("%Y-%m-%d")
#print date_N_days_ago.strftime("%Y-%m-%d")


#boto3.setup_default_session(profile_name='IAM')

resource = boto3.resource('iam')
client = boto3.client("iam")

KEY = 'LastUsedDate'

for user in resource.users.all():
    Metadata = client.list_access_keys(UserName=user.user_name)
    if Metadata['AccessKeyMetadata'] :
        for key in user.access_keys.all():
            AccessId = key.access_key_id
            Status = key.status
            LastUsed = client.get_access_key_last_used(AccessKeyId=AccessId)
            if (Status == "Active"):
                key_old = LastUsed['AccessKeyLastUsed'][KEY].strftime("%Y-%m-%d")
                if KEY in LastUsed['AccessKeyLastUsed'] and key_old <= date_90_days_ago:
                    print "User: " , user.user_name ,  "Key: " , AccessId , "AK Last Used: " , LastUsed['AccessKeyLastUsed'][KEY]
            else:
                print "User: ", user.user_name  , "Key: ",  AccessId , "Keys is InActive"
    else:
        print "User: ", user.user_name  , "No KEYS for this USER"    #".. proof: " , Metadata

