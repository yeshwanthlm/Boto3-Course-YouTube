import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam_console_resource = aws_management_console.resource('iam') # Resource Object
iam_console_client = aws_management_console.resource('iam') # Client Object

# Listiing iam users with resource object:
for each_user in iam_console_resource.users.all():
    print(each_user.name)

# Listing iam users with client object:
for each in iam_console_client.list_users()['Users']:
   print(each['UserName'])