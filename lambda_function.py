import boto3
import logging
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# AWS services
connect_client = boto3.client('connect', region_name='us-east-1')
ses_client = boto3.client('ses', region_name='us-east-1')

def send_email(email_address, user_list):
    # Replace sender@example.com with your SES sender email address.
    sender_address = 'sender@example.com'
    
    # Specify the recipient's email address.
    recipient_address = 'TEST@TEST.COM'
    
    # The subject line for the email.
    subject = "Users with Desk Phone Setting in Amazon Connect"
    
    # Create the email body.
    body = "The following users in Amazon Connect have the 'DESK_PHONE' setting:\n\n"
    body += "\n".join(user_list)
    
    # Create a multipart message to send both text and HTML versions of the email.
    msg = MIMEMultipart()
    msg['From'] = sender_address
    msg['To'] = recipient_address
    msg['Subject'] = subject

    # Attach the email body.
    msg.attach(MIMEText(body, 'plain'))

    # Try to send the email using SES.
    try:
        response = ses_client.send_raw_email(
            Source=sender_address,
            Destinations=[recipient_address],
            RawMessage={'Data': msg.as_string()}
        )
        print("Email sent successfully. Message ID:", response['MessageId'])
    except ClientError as e:
        print(f"Email sending failed: {str(e)}")

def lambda_handler(event, context):
    # Repleace with your COnnect Instance ID
    instance_id = 'AmazonConnectInstanceID'
    
    # Get the list of users in the specified Amazon Connect instance
    response = connect_client.list_users(InstanceId=instance_id)

    desk_phone_users = []

    # Print the list of users
    print("List of Users:")
    for user in response['UserSummaryList']:
        print(user['Username'])

    for user in response['UserSummaryList']:
        user_arn = user['Arn']
        
        # Use the Amazon Connect API to get user attributes
        response = connect_client.describe_user(UserId=user_arn, InstanceId=instance_id)
        
        # Check if 'User' key and 'PhoneConfig' key exist in the response
        if 'User' in response and 'PhoneConfig' in response['User']:
            phone_type = response['User']['PhoneConfig']['PhoneType']

            # Print the attributes for each user
            print(f"Phone Type for {user['Username']}: {phone_type}")

            if phone_type == 'DESK_PHONE':
                desk_phone_users.append(user['Username'])

    if desk_phone_users:
        # Notify or take action with the list of users with "DESK_PHONE" setting
        print("Users with 'DESK_PHONE' setting:")
        for username in desk_phone_users:
            print(username)
        # Define the recipient's email address here
        recipient_address = 'TEST@TEST.COM'
        
        # Send an email notification with the list of users
        send_email(recipient_address, desk_phone_users)
    else:
        print("No users found with 'DESK_PHONE' setting.")
