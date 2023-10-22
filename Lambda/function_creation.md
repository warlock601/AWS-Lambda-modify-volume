### 1. First we'll create an IAM role that we're gonna assign to this lambda function which will have appropriate permissions to change the EBS volume type.
 Create a role with default settings and then attach an Inline policy, selct EC2 as the service for inline policy, then allow these 2 actions:
- ModifyVolume
- DescribeVolumes <br />
### And for CloudWatch service allow these actions:
- CreateLogGroup
- CreateLogStream
- PutLogEvents
### 2. Now create a lambda function with Python-3 as Runtime and select the role we created using "Change default execution role" > "Use an existing role". Select the role that we just created. Then when we test this, we can see the Execution results.
### 3. Next, go to CloudWatch to configure a rule (Amazon EventBridge) that will trigger the lambda function.
- CloudWatch > Rules > Create Rule
- Select Event source = AWS events or EventBridge partner events
- AWS service = EC2, Event type = EBS Volume Notification
- Event Type = modifyVolume, createVolume
- Select Target as Lambda Function and select the function we created.
### 4. Modify the lambda function as [this](https://github.com/warlock601/AWS-Lambda-modify-volume/blob/346523b001604570bd737112ed8904b0a42100cd/Lambda/lambda_function.py), the code is elaborated below:
- First we retrieved "arn" from the event. An event is a JSON-formatted document that contains data for a Lambda function to process. The Lambda runtime converts the event to an object and passes it to your function code. It is usually of the Python dict type.
- An Event looks like this-
```bash
  {
   "version":"0",
   "id":"e5ecbf95-d0ec-c6c2-0a8a-5f362418b894",
   "detail-type":"EBS Volume Notification",
   "source":"aws.ec2",
   "account":"417623538526",
   "time":"2023-10-22T05:47:28Z",
   "region":"us-east-1",
   "resources":[
      "arn:aws:ec2:us-east-1:417623538526:volume/vol-00468ad082ab2e80d"
   ],
   "detail":{
      "result":"available",
      "cause":"",
      "event":"createVolume",
      "request-id":"b21c78c7-a3be-4e96-bc19-09d6950f9286"
   }
}
```
We can find the "arn" in "resources".
- To retrieve arn, let say we stored it's value inside a variable "volume_id"
```bash
  volume_id=event{'resources'][0]       #this will retrieve the 1st value ok key-resources which is arn
```
- Now, we will extrac the volume-ID from this arn, so we used this function:
```bash
  def getvolumeidfrom_arn(volume_arn):
    arn_parts = volume_arn.split(':')                #split the ARN using colon ":"
    volume_id = arn_parts[-1].split('/')[-1]         #the volume ID is the last part of the ARN after the 'volume/' prefix
    return volume_id
```
- Now we specify the Client value. Clients provide a low-level interface to AWS whose methods map close to 1:1 with service APIs. Client is basically used to change the poarameters here. 
```bash
   client = boto3.client('ec2')
```
For S3, we can specify it as:
```bash
  client = boto3.client('s3')
```
- Next, we use modify_volume of boto3 module to change parameters of the EBS volume.<br />
  Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts.<br />
  modify_volume : You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity.
```bash
  response = client.modify_volume(
    DryRun=True|False,
    VolumeId='string',
    Size=123,
    VolumeType='standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
    Iops=123,
    Throughput=123,
    MultiAttachEnabled=True|False
)
```
we'll modify it as (as we don't need other parameters specified as such):
```bash
  response = client.modify_volume(                # this is used to change parameters in EC2
        VolumeId = volume_id,                     # we stored the volume-ID in this variable
        VolumeType = 'gp3',                       # as we want to change whatever volume-type is there, into "gp3"
    )

```
Click on Deploy to save the function.
### 5. After Deploying, go to CloudWatch > Log Groups & there you'll see logs being logged for your Lambda function whenever any EBS volume is being created.
![Screenshot 2023-10-22 184258](https://github.com/warlock601/AWS-Lambda-modify-volume/assets/32487715/8db119f6-2980-40a6-8726-e0e030596eb4)

### 6. Now whenever any EBS volume with type "gp2" is created, it will get changed to "gp3". <br />

Before:<br />
<br />
![Screenshot 2023-10-22 184948](https://github.com/warlock601/AWS-Lambda-modify-volume/assets/32487715/8b8c4644-2ada-4e86-a825-7654b48f5b0f) <br />

After:<br />
<br />
![Screenshot 2023-10-22 185052](https://github.com/warlock601/AWS-Lambda-modify-volume/assets/32487715/b79211a7-1406-4d38-8c39-8de5f82c0114)




