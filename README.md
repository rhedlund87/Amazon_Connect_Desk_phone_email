# Amazon_Connect_Desk_phone_email
Get an email alert when users are suing the DESK_PHONE setting in amazon connect CCP or workspace
This example provides a Python 3.11 Lambda that will look at all users in Connect to find which users have their CCP set to DESK_PHONE and sned an email with that user list.
Using the DESK_PHONE in AMazon Connect incurrs additional cost for the PSTN call out, Thus a lot of call centers wish to prevent this. This option can be disabled in a custom CCP by settign the following:
enablePhoneTypeSettings: false
But if using out of the box CCP or workspace this is not an option.
INSTRUCTIONS:
Copy the code form lambda_function.py into a python 3.11 Lambda function you create in the AWS console
