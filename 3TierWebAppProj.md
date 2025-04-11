---
layout: default
title: 3-Tier Web App on AWS Fargate
---

# 🚀 3-Tier Web Application on AWS

This project showcases a production-style 3-tier architecture deployed entirely on AWS using Terraform and Docker.

## 🧱 Stack
- **Backend:** Node.js + Express (containerized)
- **Database:** Amazon RDS (PostgreSQL with SSL)
- **Infrastructure:** ECS Fargate, ALB, VPC, Terraform

## 🔎 Live Features
- `/` – Health check
- `/dbtest` – Live DB connectivity test

## 📘 Highlights
- Fully managed deployment with infrastructure as code
- Secure RDS integration with enforced SSL
- Built with Terraform modules and Docker for CI/CD readiness

[View the GitHub Repository](https://github.com/KenB773/3TierWebAppTerraform)