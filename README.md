# Amazon Connect Desk Phone Email

In Amazon Connect, agents have the option to receive calls via SOFT_PHONE or DESK_PHONE. Using the DESK_PHONE incurs additional cost for the PSTN call leg and Supervisors don't have a way to detect agents using this option.

This solution walks you through how to automatically send an email alert when users are using the DESK_PHONE setting in Amazon Connect CCP or workspace.

This example provides a Python 3.11 Lambda Function that will look at all users in Connect to find which users have their CCP set to DESK_PHONE and send an email with that user list.\
This option can be disabled in a custom CCP by settign the following:

enablePhoneTypeSettings: false\
But if using out of the box CCP or workspace this is not an option.

<h5>Instructions to setup Lambda function via CloudFormation template:</h5>
1. Set Up S3 Bucket:

Log in to the AWS console.
Navigate to the S3 service.
2. Create a New Bucket:

In the upper right-hand corner, click on "Create Bucket."
Provide a unique name for the bucket.
Scroll down and click "Create Bucket."
3. Download and Upload Python Script:

Download the index.py file.
Zip the index.py file.
Upload the zipped file to the S3 bucket created in the previous step.
4. Download CloudFormation Template:

Download the connect-agent-desk-phone-solution.yaml file.
5. Set Up CloudFormation Stack:

Navigate to the AWS console and go to the CloudFormation service.
Click on "Create stack" in the upper left-hand corner.
6. Choose Template File:

Select "With new resources (standard)."
Choose "Upload a Template."
Select the YAML file downloaded in the previous step.
Click "Next."
7. Configure Stack Details:

Provide a stack name.
Fill out the required parameters:
Connect Instance ID (Refer to how to find your Connect Instance ID).
Receipt Email.
Sender Recipient Email Address.
Sender Email Address.
Solution Source Bucket.
8. Continue Configuration:

Click "Next."
Leave stack options as default and click "Next."
9. Review and Acknowledge:

Review the settings.
Acknowledge the following:
"I acknowledge that AWS CloudFormation might create IAM resources."
"I acknowledge that AWS CloudFormation might create IAM resources with custom names."
"I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND."
10. Submit and Monitor:

After acknowledging, click "Submit."
Monitor the CloudFormation process until it completes successfully.
11. Locate Lambda Resources:

Once CloudFormation is successful, go to the "Resources" tab to locate your Lambda functions.
Congratulations! You have successfully deployed AWS resources using CloudFormation.

								   
																																																								   
																																						 
																																 
													
																																		 
																																
									

<h5>Instructions to schedule this Lambda function to run every X minutes:</h5>

1. Search in the AWS Console for the services [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/)
2.  Select EventBridge Schedule and click Create Schedule: ![EventBridge Image](Assest/EventBridge.PNG)
3. Give the Schedule a name and Description. Under schedule pattern select Recurring Schedule. Select the Schedule type as Rate-based Schedule and set the Rate to something like 15 minutes. And set Flexible time window to *Off*
4. This means the lambda will run and check for users with the DESK_PHONE settign every 15 minute. You can define how often you wish for this lambda to check.
5. Give a date and time including timezone for when you want the lambda to fist kick off. Leave End date and time blank and click next
6. Select Lambda from the list of templated targets
7. Scroll down and from the Lambda function list, select the lambda you deployed previously. Don't worry about the payload and click Skip to Review and create schedule.
9. Review and click Create Schedule.

Once everything is all set up you will receive an email with all users who have their CCP / Workspace set to use the DESK_PHONE option emailed to you:\
![example email](Assest/email_example.PNG)

