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
7.  Make sure your Lambda has the following Rights:\
      A. connect:DescribeUser\
      B. connect:ListUsers\
      C. ses:SendRawEmail
8. Now lets schedule this Lambda to run every X minutes:
9. Search in the AWS Console for the services [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/)
10. Select EventBridge Schedule and click Create Schedule: ![EventBridge Image](Assest/EventBridge.PNG)
11. Give the Schedule a name, Description, and under schedule pattern select Recurring Schedule. Select the Schedule type as Rate-based Schedule and set the Rate to something like 15 minutes. And set FLexible time window to Off
12. This means the lambda will run and check for users with the DESK_PHONE settign every 15 minutes, define how often you whish for this lambda to check.
13. Give a date and time including timezone for when you want this to fist kick off, leave End date and time blank and click next
14. Select Lambda from the list of templated targets
15. Scroll down and from the Lambda function list, select the lambda you deployed in step 6. Dont worry about the payload and click next.
16. Select Action after schedule completion as NONE, and under Retry policy and dead-letter queue (DLQ), turn it off, click next
17. Review and click Create Schedule

Once everything is all set up you will recieve and email with all users who have their CCP / Workspace set to use the DESK_PHONE option emailed to you:

