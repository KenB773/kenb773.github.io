# Silent Scalper

## 🚀 Project Summary

**Silent Scalper** is a serverless data pipeline designed to solve two common problems in cloud-based systems:

- 💸 **Wasting money on idle compute** (servers sitting idle when there’s no work to do)
- 💥 **Crashing during traffic spikes** (overloaded infrastructure from sudden file dumps)

This project uses AWS native services to create a responsive, cost-effective solution that automatically processes incoming files with zero manual provisioning.

---

## 📐 Architecture Overview

```
Uploader ──▶ S3 Bucket ──▶ Lambda Function
                                 │
                ┌────────────────┼────────────────┐
                ▼                ▼                ▼
           DynamoDB         SNS Notification   CloudWatch Logs
                │
                ▼
        Quarantine S3 Bucket (on failure)
```

---

## 🔧 Key Features

- ✅ Event-driven compute triggered on file upload
- ✅ Scales automatically — no idle infrastructure
- ✅ Writes file metadata to DynamoDB
- ✅ Sends real-time SNS alerts for success or failure
- ✅ Quarantines failed uploads to a separate S3 bucket
- ✅ CloudWatch logs for debugging and monitoring

---

## 🧰 Tech Stack

**AWS Services:**

- S3 (file upload + quarantine)
- Lambda (file processing)
- DynamoDB (metadata store)
- SNS (notifications)
- CloudWatch (logs + metrics)
- IAM (roles and permissions)

**Runtime:** Python 3.12 (AWS Lambda)

---

## 🧪 How It Works

1. A file is uploaded to the `silent-scalper-input` S3 bucket
2. S3 triggers a Lambda function
3. Lambda extracts metadata: filename, size, timestamp
4. The metadata is stored in a DynamoDB table (`FileMetadata`)
5. An SNS topic (`ScalperAlerts`) sends a notification email
6. If an error occurs, the file is moved to a quarantine bucket
7. Logs and alerts are published to CloudWatch

---

## 🔐 Security & Cost

- IAM policies follow least-privilege principle
- Entire project fits within the AWS Free Tier:
  - ✅ 1M Lambda invocations/month
  - ✅ 5GB S3 storage
  - ✅ 25GB DynamoDB storage
  - ✅ 1M SNS publishes
  - ✅ 5GB CloudWatch logs

---

## 📸 Screenshots

> *(Add screenshots here for: Lambda logs, SNS alert email, DynamoDB entry, S3 quarantine bucket, etc.)*

---

## 💬 Reflections

This project was a hands-on exploration of real-world AWS architecture patterns. I wanted to build something that responded to real problems: wasteful compute and fragile scaling. Silent Scalper uses serverless tools to build a lean, resilient, and automated system that handles high-volume file ingestion with ease.

Next steps may include:

- Adding automated retries from the quarantine bucket
- Integrating with a web dashboard for file tracking
- Logging file types and processing durations for analytics

---

## 🔗 GitHub Repository

> [GitHub Link Here]

## 🗺️ Architecture Diagram

>

*(Or insert draw\.io / Lucidchart link if interactive)*

