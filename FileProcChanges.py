import os, time

start = time.time()

file_type = os.path.splitext(key)[1].lower()
duration = round(time.time() - start, 3)

# DynamoDB put_item:
'FileType': file_type,
'Duration': duration
