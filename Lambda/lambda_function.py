import boto3

def getvolumeidfrom_arn(volume_arn):
    arn_parts = volume_arn.split(':')                #split the ARN using colon ":"
    volume_id = arn_parts[-1].split('/')[-1]         #the volume ID is the last part of the ARN after the 'volume/' prefix
    return volume_id

def lambda_handler(event, context):
    
    
    volume_arn = event['resources'][0]
    volume_id = getvolumeidfrom_arn(volume_arn)
    
    ec2_client = boto3.client('ec2')

    response = ec2_client.modify_volume(            #this is used to change parameters in EC2
        VolumeId = volume_id,
        VolumeType = 'gp3',
    )

    
