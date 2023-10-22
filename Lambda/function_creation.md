### 1. First we'll create an IAM role that we're gonna assign to this lambda function which will have appropriate permissions to change the EBS volume type.
 Create a role with default settings and then attach an Inline policy, selct EC2 as the service for inline policy, then allow these 2 actions:
- ModifyVolume
- DescribeVolumes <br />
### And for CloudWatch service allow these actions:
- CreateLogGroup
- CreateLogStream
- PutLogEvents
### 2. Now create a lambda function with Python-3 as Runtime and select the role we created using "Change default execution role" > "Use an existing role". Select the role that we just created. Then when we test this, we can see the Execution results.
### 3. Next, go to CloudWatch to configure a rule that will trigger the lambda function.
- CloudWatch > Rules > Create Rule
- Select Event source = AWS events or EventBridge partner events
- AWS service = EC2, Event type = EBS Volume Notification
- Event Type = modifyVolume, createVolume
- Select Target as Lambda Function
### 4. 
