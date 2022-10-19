# Import all the modules and Libraries
import boto3
# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")
# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
result = ec2_console.describe_instances()['Reservations']
for each_instance in result:
    for value in each_instance['Instances']:
        print(value['InstanceId'])
