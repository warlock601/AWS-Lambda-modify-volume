### 1. First we'll create an IAM role that we're gonna assign to this lambda function which will have appropriate permissions to change the EBS volume type.
 Create a role with default settings and then attach an Inline policy, selct EC2 as the service for inline policy, then allow these 2 actions:
- ModifyVolume
- DescribeVolumes
### 2. Now create a lambda function with Python-3 as Runtime and select the role we created using "Change default execution role" > "Use an existing role". Then when we test this, an event will be created. We can see the Execution results after we tested this.
### 3. Next, go to CloudWatch to configure a rule that will trigger the lambda function
