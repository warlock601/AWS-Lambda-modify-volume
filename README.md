# AWS-Lambda-modify-volume Project Description

As a DevOps engineer, it's our responsibility to take care of the infrastructure and make sure it is in compliance with the organizational policies. Let say our company have attached GP2 type EBS volumes to all the instances but now they want to change to GP3 and even if any new instances are created, they also have GP3 type volumes attached to them by default. 
</br>
<br/>
So here we'll use AWS CloudWatch in combination with AWS Lambda to govern the resources according to the policies. We'll trigger a Lambda function whenever any EBS voilume is created and with the help of CloudWatch Events, we'll monitor and respond to EBS volumes that are of type GP2 and convert them to type GP3. For the existing ones, we'll verify using AWS Lambda whether it is of type GP3 or not, if it's not then we automatically convert into GP3 type. Inside AWS Lambda functions, we'll use Python as scripting language.
<br/>
<br/>
We can do this for any service, let say for S3, EKS etc. and make sure that our infrastrcuture is in compliance with the organizational policies.

## Tech Stack:

**AWS Lambda**  <br/>
**AWS CloudWatch** <br/>
**Python** <br />
<br />
![arch](https://github.com/warlock601/AWS-Lambda-modify-volume/assets/32487715/114855d3-108f-4fce-8651-f65723e0e730)


 We'll start from [here](https://github.com/warlock601/AWS-Lambda-modify-volume/blob/1c5e3549f280bdda3be67654ffe32bbfe07474e2/Lambda/function_creation.md)
