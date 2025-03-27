import boto3
import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print("Starting snapshot job...")

    instances = ec2.describe_instances(
        Filters=[{'Name': 'tag:backup', 'Values': ['true']}]
    )

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            print(f"Found instance: {instance_id}")

            for mapping in instance.get('BlockDeviceMappings', []):
                volume_id = mapping['Ebs']['VolumeId']
                now = datetime.datetime.utcnow()
                snapshot_name = f"{instance_id}-{volume_id}-{now.strftime('%Y%m%d-%H%M%S')}"

                print(f"Creating snapshot for volume {volume_id}")
                ec2.create_snapshot(
                    VolumeId=volume_id,
                    Description="Auto backup by Smart Vault",
                    TagSpecifications=[
                        {
                            'ResourceType': 'snapshot',
                            'Tags': [
                                {'Key': 'Name', 'Value': snapshot_name},
                                {'Key': 'CreatedBy', 'Value': 'SmartVault'},
                                {'Key': 'InstanceId', 'Value': instance_id}
                            ]
                        }
                    ]
                )
    print("Snapshot job complete.")