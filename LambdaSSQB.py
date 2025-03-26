import boto3
import os
import json
import time

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TABLE_NAME = 'SS-FileMetadata'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:471303021226:SSAlerts'
QUARANTINE_BUCKET = 'silent-scalper-quarantine-test'

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object'].get('size', 0)

        try:
            # Store metadata in DynamoDB
            table = dynamodb.Table(TABLE_NAME)
            table.put_item(Item={
                'FileName': key,
                'Size': size,
                'Bucket': bucket,
                'TimeStamp': int(time.time())
            })

            # Send success alert
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=f"✅ File processed: {key}\nSize: {size} bytes\nBucket: {bucket}",
                Subject="Silent Scalper: Success"
            )

        except Exception as e:
            try:
                # Copy to quarantine bucket
                s3.copy_object(
                    CopySource={'Bucket': bucket, 'Key': key},
                    Bucket=QUARANTINE_BUCKET,
                    Key=key
                )

                # Optional: Delete original
                # s3.delete_object(Bucket=bucket, Key=key)

                # Send quarantine alert
                sns.publish(
                    TopicArn=SNS_TOPIC_ARN,
                    Message=f"🚨 Failed to process file: {key}\nError: {str(e)}\nMoved to quarantine bucket.",
                    Subject="Silent Scalper: File Quarantined"
                )

            except Exception as quarantine_error:
                print(f"🚨 Quarantine process also failed: {quarantine_error}")

        print(f"Processed file: {key}")
