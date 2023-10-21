# AWS-Ninja

As a DevOps engineer, it's our responsibility to take care of the infrastructure and make sure it is in compliance with the organizational policies. Let say our company have attached GP2 type EBS volumes to all the instances but now they want to change to GP3 and even if any new instances are created, they also have GP3 type volumes attached to them by default. 
</br>
<br/>
So here we'll use AWS CloudWatch in combinagtion with AWS Lambda to govern the resources according to the policies. We'll trigger a Lambda function whenever any EBS voilume is created and with the help of CloudWatch Events, we'll monitor and respond to EBS volumes that are of type GP2 and convert them to type GP3.
