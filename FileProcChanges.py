import os, time

start = time.time()

# ...existing code...

file_type = os.path.splitext(key)[1].lower()
duration = round(time.time() - start, 3)

# Include these in your DynamoDB put_item:
'FileType': file_type,
'Duration': duration
