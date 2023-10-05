# Amazon Connect Desk Phone Email

In Amazon Connect, agents have the option to receive calls via SOFT_PHONE or DESK_PHONE. Using the DESK_PHONE incurs additional cost for the PSTN call leg and Supervisors don't have a way to detect agents using this option.

This solution walks you through how to automatically send an email alert when users are using the DESK_PHONE setting in Amazon Connect CCP or workspace.

This example provides a Python 3.11 Lambda Function that will look at all users in Connect to find which users have their CCP set to DESK_PHONE and send an email with that user list.\
This option can be disabled in a custom CCP by settign the following:\

enablePhoneTypeSettings: false\
But if using out of the box CCP or workspace this is not an option.\

<h5>Instructions to setup Lambda function:</h5>

1.  Copy the code from lambda_function.py into a python 3.11 Lambda function you create in the AWS console \ **NOTE:** lines 8 and 9 reference us-east-1 if you are not working in that region please updat those to the needed region
2.  Edit Line 13 and replace sender@example.com with your SES sender email address
3.  Edit Line 16 and replace recipient@example.com with the recipient address you desire.
4.  Edit Line 46 and replace YOUR_CONNECT_INSTANCE_ID with your Amazon Connect Instance ID.     [How to find your Connect Instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html)
5.  Edit Line 81 and replace recipient@example.com with the recipient address you used on line 16.
6.  Deploy your Lambda
7.  Make sure your Lambda has the following IAM Permissions:\
      A. connect:DescribeUser\
      B. connect:ListUsers\
      C. ses:SendRawEmail
														
																										  
																									   
																																																								   
																																						 
																																 
													
																																		 
																																
									

<h5>Instructions to schedule this Lambda function to run every X minutes:</h5>

1. Search in the AWS Console for the services [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/)
2.  Select EventBridge Schedule and click Create Schedule: ![EventBridge Image](Assest/EventBridge.PNG)
3. Give the Schedule a name and Description. Under schedule pattern select Recurring Schedule. Select the Schedule type as Rate-based Schedule and set the Rate to something like 15 minutes. And set Flexible time window to *Off*
4. This means the lambda will run and check for users with the DESK_PHONE settign every 15 minute. You can define how often you wish for this lambda to check.
5. Give a date and time including timezone for when you want the lambda to fist kick off. Leave End date and time blank and click next
6. Select Lambda from the list of templated targets
7. Scroll down and from the Lambda function list, select the lambda you deployed in step 6. Don't worry about the payload and click next.
8. Select Action after schedule completion as NONE, and under Retry policy and dead-letter queue (DLQ), turn it off, click next
9. Review and click Create Schedule.

Once everything is all set up you will receive an email with all users who have their CCP / Workspace set to use the DESK_PHONE option emailed to you:\
![example email](Assest/email_example.PNG)

