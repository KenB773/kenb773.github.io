<head>
  <script src="https://cdn.tailwindcss.com"></script>
</head>

<style>
    .cyber-gradient {
        background: linear-gradient(135deg, #1e293b 0%, #1b1b1b 50%, #1a1a1a 100%);
    }
    .neon-text {
        text-shadow: 0 0 5px #3b82f6, 0 0 10px #3b82f6;
    }
    .card-hover {
        transition: all 0.3s ease;
    }
    .card-hover:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    .terminal {
        background-color: #0f172a;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        position: relative;
    }
    .terminal-header {
        background-color: #1e293b;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        padding: 8px 15px;
    }
    .terminal-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
    }
    .terminal-content {
        padding: 20px;
        color: #e2e8f0;
        font-size: 14px;
        line-height: 1.6;
    }
    .command {
        color: #10b981;
    }
    .response {
        color: #e2e8f0;
    }
    .cursor {
        display: inline-block;
        width: 10px;
        height: 18px;
        background-color: #e2e8f0;
        animation: blink 1s infinite;
    }
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    .hexagon {
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    }
</style>

<!-- Hero Section -->
<section class="cyber-gradient py-20 px-6">
    <div class="container mx-auto flex flex-col md:flex-row items-center">
        <div class="md:w-1/2 mb-10 md:mb-0">
            <h1 class="text-4xl md:text-5xl font-bold mb-4 neon-text">Building & Securing a Cloud-Enabled, AI-Powered Future</h1>
            <p class="text-xl text-blue-200 mb-8">Cybersecurity | Cloud Operations & Security | Dev(Sec)Ops Engineer | AI/ML Ops </p>
        </div>
        <div class="md:w-1/2 flex justify-center">
            <div class="terminal w-full max-w-md">
                <div class="terminal-header">
                    <span class="terminal-dot bg-red-500"></span>
                    <span class="terminal-dot bg-yellow-500"></span>
                    <span class="terminal-dot bg-green-500"></span>
                </div>
                <div class="terminal-content">
                    <p><span class="command">$ whoami</span></p>
                    <p class="response mb-4">Ken Brigham - Security & Cloud Specialist</p>
                    <p><span class="command">$ skills --cybersecurity --cloud --devsecops --ai</span></p>
                    <p class="response mb-4">Cybersecurity | Cloud Operations & Security | Dev(Sec)Ops Engineer | AI/ML Ops</p>
                    <p><span class="command">$ contact --method=email</span></p>
                    <p class="response">kenbrigham777@gmail.com</p>
                    <p><span class="command">$ _</span><span class="cursor"></span></p>
                </div>
            </div>
        </div>
    </div>
</section>

Welcome - here you'll find my many projects! What started out as a focused page to document cybersecurity work has evolved into much more - Dev(Sec)Ops, CI/CD, Full-Stack Web Development, Cloud Architecture & Engineering, Cloud Security, Software Development and of course, AI/ML. This has become something of a playground, workshop, and a digital map of where curiosity has led (and continues to lead) me. Thanks for checking it out.

## Projects

### [Quick Incident Triage Toolkit](https://github.com/KenB773/QuickIncidentTriageToolkit) - A sleek, offline desktop app built with Rust, Tauri, and React for rapid system diagnostics. It visualizes real-time CPU, memory, disk, network, and process activity, and supports one-click data export to JSON.

### [AWS 3-Tier Web App](3TierWebAppProj.md) - A full-stack, 3-tier Node.js web application on AWS using ECS Fargate, ALB, and RDS PostgreSQL, fully provisioned through Terraform and containerized with Docker. The project includes health checks, secure DB connectivity via SSL, and modular infrastructure-as-code for production-style scalability.

### [AWS/GCP 'KubeCart' project](KubeCartProj.md) - KubeCart is a containerized Flask microservice simulating a basic shopping cart API, deployed to AWS using Kubernetes (EKS) and exposed via a public Load Balancer. It features a live Swagger UI for testing endpoints, built using Flask-RESTX and deployed with Docker, eksctl, and kubectl.

### [Automated CI/CD Security Scan Pipeline](https://github.com/KenB773/SecurityScanPipeline) - A GitHub Actions pipeline that integrates Trivy, Checkov, Bandit, and OWASP Dependency-Check to automatically scan code, containers, and infrastructure for vulnerabilities — complete with SARIF reporting for GitHub Security.

### [Azure Home SOC Setup](homesoc.md) - My Home SOC is a functional personal cloud security operations center built on Azure services, featuring log ingestion with Log Analytics, real-time alerting via Azure Monitor, and custom detection rules for tracking suspicious activity across a simulated home network.

### [RogueSpeared tool](https://github.com/KenB773/RogueSpeared) - A red-team proof-of-concept tool that creates 'polyglot' files combining real WAV audio with XOR-encrypted Python payloads. The resulting file plays as normal audio but also executes embedded code when run as a script.

### [AWS PartyRock - JargonBridge GenAI App](https://partyrock.aws/u/KenB7/1nIRFrtOV/JargonBridge) - A fun little Gen AI PartyRock tool I created for bidirectionally converting technical jargon and plain english. Includes a basic Claude-powered chatbot that can answer questions about terms used and its thought process behind the 'translations'.
-  [Example input/output snapshot](https://partyrock.aws/u/KenB7/1nIRFrtOV/JargonBridge/snapshot/jHsfSVHf4)

### [AWS 'Silent Scalper' project](SilentScalperProj.md) - Serverless data pipeline. Using event-driven AWS architecture, my 'Silent Scalper' processes incoming files the moment they’re uploaded (without pre-provisioned infrastructure), scales automatically, and gracefully handles both success and failure paths. Aims to eliminate idle compute waste, as well as file loss resulting from crashes during unpredictable traffic spikes.

### [AWS 'Smart Vault' project](SmartVaultProj.md) - Serverless AWS automation tool - my 'Smart Vault' is used to create, tag, and manage EBS snapshots for EC2 instances based on resource tags. It features scheduled backups, audit logging via DynamoDB, and automated cleanup to reduce storage costs.

### [TryHackMe SOC Level 1](thmsoclevel1.md)

## Resume + Credentials
### [Resume](Resume New.pdf)
### [Credly Profile](https://www.credly.com/users/mackenzie-brigham)

