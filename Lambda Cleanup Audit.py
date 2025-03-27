import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
audit_table = dynamodb.Table('SmartVaultCleanupAudit')

# Inside your snapshot deletion loop:
# After ec2.delete_snapshot(...)
audit_table.put_item(Item={
    'SnapshotId': snapshot_id,
    'DeletedAt': datetime.utcnow().isoformat(),
    'InstanceId': next((t['Value'] for t in snapshot.get('Tags', []) if t['Key'] == 'InstanceId'), 'unknown'),
    'Retention': RETENTION_DAYS
})