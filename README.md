# Amazon_Connect_Desk_phone_email
Get an email alert when users are suing the DESK_PHONE setting in amazon connect CCP or workspace\
This example provides a Python 3.11 Lambda that will look at all users in Connect to find which users have their CCP set to DESK_PHONE and send an email with that user list.\
Using the DESK_PHONE in Amazon Connect incurrs additional cost for the PSTN call out, Thus a lot of call centers wish to prevent this. This option can be disabled in a custom CCP by settign the following:\
enablePhoneTypeSettings: false\
But if using out of the box CCP or workspace this is not an option.\
INSTRUCTIONS:\
1.  Copy the code from lambda_function.py into a python 3.11 Lambda function you create in the AWS console
2.  Edit Line 13 and Replace sender@example.com with your SES sender email address
3.  Edit Line 16 and Replace recipient@example.com with the receipient address you desire.
4.  Edit Line 46 and Repalce YOUR_CONNECT_INSTANCE_ID with your Amazon Connect Instance ID.     [How to find your Connect Instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html)
5.  Edit Line 81 Replace recipient@example.com with the receipient address you used on line 16.
6.  Deploy your Lambda
7.  Make sure your Lambda has the following Rights:/
      A. connect:DescribeUser/
      B. connect:ListUsers/
      C. ses:SendRawEmail/
8.

