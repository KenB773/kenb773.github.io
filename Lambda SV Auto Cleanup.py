import boto3
import datetime

# AWS clients
ec2 = boto3.client('ec2')
dynamodb = boto3.resource('dynamodb')
audit_table = dynamodb.Table('SmartVaultCleanupAudit')

# Keep snapshots for this many days
RETENTION_DAYS = 7

def lambda_handler(event, context):
    print(f"Looking for SmartVault snapshots older than {RETENTION_DAYS} days...")

    # Calculate cutoff date
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    cutoff = now - datetime.timedelta(days=RETENTION_DAYS)

    # Find SmartVault snapshots
    snapshots = ec2.describe_snapshots(
        Filters=[{'Name': 'tag:CreatedBy', 'Values': ['SmartVault']}],
        OwnerIds=['self']
    )['Snapshots']

    deleted_count = 0

    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        start_time = snapshot['StartTime']

        if start_time < cutoff:
            print(f"Deleting snapshot {snapshot_id} (created {start_time})")
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            deleted_count += 1

            # Get InstanceId tag (if it exists)
            instance_id = next(
                (t['Value'] for t in snapshot.get('Tags', []) if t['Key'] == 'InstanceId'),
                'unknown'
            )

            # Log deletion in DynamoDB
            audit_table.put_item(Item={
                'SnapshotId': snapshot_id,
                'DeletedAt': now.isoformat(),
                'InstanceId': instance_id,
                'Retention': RETENTION_DAYS
            })

    print(f"Cleanup complete. Deleted {deleted_count} snapshot(s).")
