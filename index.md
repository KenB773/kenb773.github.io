<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ken Brigham - Security Engineer</title>
  <meta name="description" content="Security engineer focused on cloud, DevSecOps, and automation. Detection tooling, hardened pipelines, and IaC for regulated environments.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg-deep: #0d1117;
      --bg-panel: #131720;
      --bg-card: #1a1f2b;
      --accent: #3b82f6;
      --accent-soft: rgba(59, 130, 246, 0.15);
    }
    html { scroll-behavior: smooth; }
    body { background-color: var(--bg-deep); }
    section[id] { scroll-margin-top: 80px; }

    .cyber-gradient {
      background:
        radial-gradient(1200px 600px at 80% -10%, rgba(59,130,246,0.12), transparent 60%),
        radial-gradient(900px 500px at 0% 110%, rgba(16,185,129,0.08), transparent 60%),
        linear-gradient(135deg, #0f1320 0%, #11151f 50%, #0d1117 100%);
    }
    .neon-text { text-shadow: 0 0 6px rgba(59,130,246,0.55), 0 0 14px rgba(59,130,246,0.35); }
    .card-hover { transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease; }
    .card-hover:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgba(59, 130, 246, 0.18); border-color: rgba(59,130,246,0.4); }

    .terminal { background-color: #0b1020; border-radius: 10px; font-family: 'Courier New', monospace; box-shadow: 0 10px 40px rgba(0,0,0,0.4); }
    .terminal-header { background-color: #1e293b; border-top-left-radius: 10px; border-top-right-radius: 10px; padding: 8px 14px; }
    .terminal-dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 6px; }
    .terminal-content { padding: 20px; color: #e2e8f0; font-size: 14px; line-height: 1.6; }
    .command { color: #10b981; }
    .response { color: #e2e8f0; }
    .cursor { display: inline-block; width: 10px; height: 18px; background-color: #e2e8f0; animation: blink 1s infinite; vertical-align: middle; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

    .bg-custom-dark { background-color: var(--bg-panel); }
    .panel-card { background-color: var(--bg-card); border: 1px solid rgba(148,163,184,0.08); }
    .chip { display: inline-block; padding: 2px 8px; border-radius: 9999px; font-size: 11px; line-height: 1.4; background: var(--accent-soft); color: #93c5fd; border: 1px solid rgba(59,130,246,0.25); margin-right: 4px; margin-bottom: 4px; }
    .featured-badge { display: inline-flex; align-items: center; gap: 4px; font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #fbbf24; background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.3); padding: 2px 8px; border-radius: 9999px; }
    .section-eyebrow { letter-spacing: 0.18em; font-size: 12px; color: #60a5fa; text-transform: uppercase; }

    a:focus-visible, button:focus-visible, summary:focus-visible { outline: 2px solid #60a5fa; outline-offset: 2px; border-radius: 4px; }

    .group-heading { display: flex; align-items: center; gap: 12px; color: #e2e8f0; font-weight: 600; font-size: 1.25rem; }
    .group-heading::before { content: ""; width: 6px; height: 22px; background: linear-gradient(180deg, #3b82f6, #10b981); border-radius: 2px; }
    .group-heading .group-sub { font-size: 12px; color: #94a3b8; font-weight: 400; letter-spacing: 0.04em; }

    details > summary { list-style: none; cursor: pointer; }
    details > summary::-webkit-details-marker { display: none; }
    details[open] .summary-chevron { transform: rotate(180deg); }
    .summary-chevron { transition: transform 0.2s ease; }

    .meta-line { color: #cbd5e1; }
    .meta-line .dot { color: #475569; margin: 0 8px; }
  </style>
</head>
<body class="bg-gray-900 text-gray-100 font-sans">

<!-- Navigation -->
<nav class="cyber-gradient py-4 px-6 sticky top-0 z-50 shadow-lg backdrop-blur">
  <div class="container mx-auto flex justify-between items-center">
    <a href="#top" class="flex items-center space-x-2">
      <i class="fas fa-shield-halved text-blue-400 text-2xl" aria-hidden="true"></i>
      <span class="text-xl font-bold">Ken Brigham</span>
    </a>
    <div class="flex flex-wrap gap-x-6 gap-y-1 text-sm md:text-base">
      <a href="#projects" class="hover:text-blue-300 transition">Projects</a>
      <a href="#certifications" class="hover:text-blue-300 transition">Certifications</a>
      <a href="#education" class="hover:text-blue-300 transition">Education</a>
      <a href="#contact" class="hover:text-blue-300 transition">Contact</a>
    </div>
  </div>
</nav>

<!-- Hero Section -->
<section id="top" class="cyber-gradient py-20 px-6">
  <div class="container mx-auto flex flex-col md:flex-row items-center gap-10">
    <div class="md:w-1/2">
      <p class="section-eyebrow mb-3">Ken Brigham</p>
      <h1 class="text-4xl md:text-5xl font-bold mb-4 neon-text">Security Engineer &mdash; Cloud, DevSecOps, and Automation</h1>
      <p class="meta-line text-base md:text-lg mb-2">
        <i class="fas fa-id-badge text-blue-400 mr-2" aria-hidden="true"></i>Sponsored for a U.S. government security clearance, currently in adjudication
      </p>
      <p class="meta-line text-base md:text-lg mb-8">
        <i class="fas fa-location-dot text-blue-400 mr-2" aria-hidden="true"></i>Open to remote and hybrid security engineering roles
      </p>
      <div class="flex flex-wrap gap-3">
        <a href="#projects" class="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2.5 rounded-md font-medium transition">View Projects</a>
        <a href="#contact" class="border border-blue-400/60 hover:border-blue-300 text-blue-200 px-5 py-2.5 rounded-md font-medium transition">Get in Touch</a>
        <a href="https://github.com/KenB773" target="_blank" rel="noopener" class="border border-gray-600 hover:border-gray-400 text-gray-200 px-5 py-2.5 rounded-md font-medium transition">
          <i class="fab fa-github mr-2" aria-hidden="true"></i>GitHub
        </a>
      </div>
    </div>
    <div class="md:w-1/2 flex justify-center w-full">
      <div class="terminal w-full max-w-md">
        <div class="terminal-header">
          <span class="terminal-dot bg-red-500"></span>
          <span class="terminal-dot bg-yellow-500"></span>
          <span class="terminal-dot bg-green-500"></span>
        </div>
        <div class="terminal-content">
          <p><span class="command">$ whoami</span></p>
          <p class="response mb-4">Ken Brigham &mdash; Security Engineer</p>
          <p><span class="command">$ focus --areas</span></p>
          <p class="response mb-4">Cloud Security · DevSecOps · Detection &amp; Response · Automation</p>
          <p><span class="command">$ clearance --status</span></p>
          <p class="response mb-4">U.S. government &mdash; sponsored, in adjudication</p>
          <p><span class="command">$ contact --method=email</span></p>
          <p class="response">kenbrigham777@gmail.com</p>
          <p><span class="command">$ _</span><span class="cursor"></span></p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Projects Section -->
<section id="projects" class="py-20 px-6 bg-custom-dark">
  <div class="container mx-auto">
    <p class="section-eyebrow mb-2 text-center">Selected Work</p>
    <h2 class="text-3xl md:text-4xl font-bold mb-3 text-center">Projects</h2>
    <p class="text-gray-400 text-center max-w-2xl mx-auto mb-14">Grouped by capability so each piece of work speaks to a specific part of the security engineering stack.</p>

    <!-- Detection & Response -->
    <div class="mb-14">
      <div class="mb-6">
        <h3 class="group-heading"><span>Detection &amp; Response</span></h3>
        <p class="group-sub mt-2 ml-[18px] text-sm text-gray-400">SOC tooling, telemetry pipelines, host artifacts, and adversary tradecraft.</p>
      </div>
      <div class="grid lg:grid-cols-2 gap-6">

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">IR · Desktop</span>
            <span class="featured-badge"><i class="fas fa-star text-[10px]" aria-hidden="true"></i> Featured</span>
          </div>
          <h4 class="text-xl font-bold mb-2">Quick Incident Triage Toolkit</h4>
          <p class="text-gray-300 mb-4 flex-grow">Offline desktop app for rapid system diagnostics &mdash; real-time monitoring, host artifact collection, and JSON export for handoff to IR teams.</p>
          <div class="mb-4"><span class="chip">Rust</span><span class="chip">Tauri</span><span class="chip">React</span><span class="chip">IR Tooling</span></div>
          <a href="https://github.com/KenB773/QuickIncidentTriageToolkit" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">SOC · Azure</span>
            <span class="featured-badge"><i class="fas fa-star text-[10px]" aria-hidden="true"></i> Featured</span>
          </div>
          <h4 class="text-xl font-bold mb-2">Home SOC on Azure</h4>
          <p class="text-gray-300 mb-4 flex-grow">A working personal SOC built on Azure Monitor, Log Analytics, and Sentinel &mdash; ingesting telemetry from a home lab and detecting simulated threats end-to-end.</p>
          <div class="mb-4"><span class="chip">Azure Sentinel</span><span class="chip">Log Analytics</span><span class="chip">KQL</span><span class="chip">SIEM</span></div>
          <a href="homesoc.html" class="text-blue-400 hover:underline font-medium">View Details <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Red Team · PoC</span>
          </div>
          <h4 class="text-xl font-bold mb-2">'RogueSpeared' Tool</h4>
          <p class="text-gray-300 mb-4 flex-grow">Red-team PoC creating polyglot WAV+Python files that play audio but execute encrypted payloads when run as scripts.</p>
          <div class="mb-4"><span class="chip">Red Team</span><span class="chip">Python</span><span class="chip">Polyglot</span></div>
          <a href="https://github.com/KenB773/RogueSpeared" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Blue Team · Lab</span>
          </div>
          <h4 class="text-xl font-bold mb-2">TryHackMe SOC Level 1</h4>
          <p class="text-gray-300 mb-4 flex-grow">Blue-team training notes and lab walkthroughs from the TryHackMe SOC Level 1 path &mdash; SIEM, threat intel, and IR fundamentals.</p>
          <div class="mb-4"><span class="chip">SOC</span><span class="chip">Blue Team</span><span class="chip">SIEM</span></div>
          <a href="thmsoclevel1.html" class="text-blue-400 hover:underline font-medium">View Notes <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

      </div>
    </div>

    <!-- Cloud Security Engineering -->
    <div class="mb-14">
      <div class="mb-6">
        <h3 class="group-heading"><span>Cloud Security Engineering</span></h3>
        <p class="group-sub mt-2 ml-[18px] text-sm text-gray-400">IaC, hardened workloads, and AWS-native automation patterns.</p>
      </div>
      <div class="grid lg:grid-cols-2 gap-6">

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Cloud · IaC</span>
            <span class="featured-badge"><i class="fas fa-star text-[10px]" aria-hidden="true"></i> Featured</span>
          </div>
          <h4 class="text-xl font-bold mb-2">AWS 3-Tier Web App</h4>
          <p class="text-gray-300 mb-4 flex-grow">Production-style Node.js 3-tier app deployed to AWS Fargate with PostgreSQL and an ALB &mdash; fully provisioned via Terraform with Docker containerization.</p>
          <div class="mb-4"><span class="chip">AWS Fargate</span><span class="chip">Terraform</span><span class="chip">Docker</span><span class="chip">PostgreSQL</span></div>
          <a href="https://github.com/KenB773/3TierWebAppTerraform" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Drift · Go</span>
          </div>
          <h4 class="text-xl font-bold mb-2">AWS IaC Drift Detector</h4>
          <p class="text-gray-300 mb-4 flex-grow">A Go-based CLI tool that detects configuration drift between Terraform-managed infrastructure and live AWS resource state.</p>
          <div class="mb-4"><span class="chip">Go</span><span class="chip">Terraform</span><span class="chip">AWS</span></div>
          <a href="https://github.com/KenB773?tab=repositories" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Serverless · Backup</span>
          </div>
          <h4 class="text-xl font-bold mb-2">AWS Smart Vault</h4>
          <p class="text-gray-300 mb-4 flex-grow">Backup management for EBS snapshots using EventBridge and Lambda &mdash; with audit logs and cleanup automation.</p>
          <div class="mb-4"><span class="chip">Lambda</span><span class="chip">EBS</span><span class="chip">EventBridge</span></div>
          <a href="smart-vault.html" class="text-blue-400 hover:underline font-medium">View Details <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Serverless · Scale</span>
          </div>
          <h4 class="text-xl font-bold mb-2">AWS Silent Scalper</h4>
          <p class="text-gray-300 mb-4 flex-grow">Serverless AWS pipeline that triggers processing on file upload with autoscaling &mdash; no idle compute.</p>
          <div class="mb-4"><span class="chip">Lambda</span><span class="chip">S3</span><span class="chip">EventBridge</span></div>
          <a href="silent-scalper.html" class="text-blue-400 hover:underline font-medium">View Details <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

      </div>
    </div>

    <!-- DevSecOps & Automation -->
    <div class="mb-14">
      <div class="mb-6">
        <h3 class="group-heading"><span>DevSecOps &amp; Automation</span></h3>
        <p class="group-sub mt-2 ml-[18px] text-sm text-gray-400">Hardened pipelines, security gates, and platform-level automation.</p>
      </div>
      <div class="grid lg:grid-cols-2 gap-6">

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">CI/CD · Security</span>
          </div>
          <h4 class="text-xl font-bold mb-2">Security Scan CI/CD Pipeline</h4>
          <p class="text-gray-300 mb-4 flex-grow">GitHub Actions pipeline integrating Trivy, Checkov, Bandit, and OWASP Dependency-Check with SARIF reporting to GitHub Security.</p>
          <div class="mb-4"><span class="chip">GitHub Actions</span><span class="chip">Trivy</span><span class="chip">Checkov</span><span class="chip">SARIF</span></div>
          <a href="https://github.com/KenB773/SecurityScanPipeline" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Azure · CI/CD</span>
          </div>
          <h4 class="text-xl font-bold mb-2">Azure DevOps Pipeline</h4>
          <p class="text-gray-300 mb-4 flex-grow">Terraform deployments at scale using Azure DevOps, Service Principals, and secured CI/CD pipelines.</p>
          <div class="mb-4"><span class="chip">Azure DevOps</span><span class="chip">Terraform</span><span class="chip">CI/CD</span></div>
          <a href="https://github.com/KenB773/AzureDevOpsPipeline" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">EKS · Jenkins</span>
          </div>
          <h4 class="text-xl font-bold mb-2">Chatbot UI on EKS</h4>
          <p class="text-gray-300 mb-4 flex-grow">OpenAI Chatbot UI deployed with Jenkins, EKS, and Terraform &mdash; built with DevSecOps practices baked in.</p>
          <div class="mb-4"><span class="chip">Jenkins</span><span class="chip">EKS</span><span class="chip">Terraform</span></div>
          <a href="https://github.com/KenB773/ChatbotUIJenkins" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Kubernetes · Microservices</span>
          </div>
          <h4 class="text-xl font-bold mb-2">KubeCart (AWS / GCP)</h4>
          <p class="text-gray-300 mb-4 flex-grow">Containerized Flask microservice deployed on EKS with a live Swagger UI for API interaction.</p>
          <div class="mb-4"><span class="chip">Kubernetes</span><span class="chip">Flask</span><span class="chip">Swagger</span></div>
          <a href="https://github.com/KenB773/KubeCart" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Project <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

      </div>
    </div>

    <!-- AI/ML Security -->
    <div>
      <div class="mb-6">
        <h3 class="group-heading"><span>AI / ML Security</span></h3>
        <p class="group-sub mt-2 ml-[18px] text-sm text-gray-400">LLM tooling and adversarial AI tradecraft.</p>
      </div>
      <div class="grid lg:grid-cols-2 gap-6">

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">LLM · App</span>
          </div>
          <h4 class="text-xl font-bold mb-2">AWS PartyRock: JargonBridge</h4>
          <p class="text-gray-300 mb-4 flex-grow">An LLM-powered app that translates technical jargon to plain English and back, built on Amazon PartyRock / Bedrock.</p>
          <div class="mb-4"><span class="chip">PartyRock</span><span class="chip">LLM</span><span class="chip">Bedrock</span></div>
          <a href="https://partyrock.aws/u/KenB7/1nIRFrtOV/JargonBridge" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View App <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

        <article class="panel-card rounded-xl p-6 card-hover flex flex-col">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs uppercase tracking-wider text-blue-300">Credential · AI Red Team</span>
          </div>
          <h4 class="text-xl font-bold mb-2">HTB &amp; Google AI Red Teamer</h4>
          <p class="text-gray-300 mb-4 flex-grow">Joint HackTheBox &amp; Google credential covering adversarial ML, prompt injection, model evasion, and AI system attack surfaces.</p>
          <div class="mb-4"><span class="chip">AI Red Team</span><span class="chip">Adversarial ML</span><span class="chip">Prompt Injection</span></div>
          <a href="https://academy.hackthebox.com/achievement/badge/7d790823-39c5-11f0-bcfd-bea50ffe6cb4" target="_blank" rel="noopener" class="text-blue-400 hover:underline font-medium">View Credential <i class="fas fa-arrow-right text-xs ml-1" aria-hidden="true"></i></a>
        </article>

      </div>
    </div>

  </div>
</section>

<!-- Certifications Section -->
<section id="certifications" class="py-20 px-6">
  <div class="container mx-auto">
    <p class="section-eyebrow mb-2 text-center">Verified Credentials</p>
    <h2 class="text-3xl md:text-4xl font-bold mb-3 text-center">Certifications</h2>
    <p class="text-gray-400 text-center max-w-2xl mx-auto mb-12">30+ industry certifications across security, cloud, and DevOps.</p>

    <!-- Visible: top 6 -->
    <div class="grid md:grid-cols-3 gap-4 mb-8">

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-certificate text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.credly.com/badges/ba475443-2a41-4c31-8874-bc547b68f85b/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">CompTIA Security+</a>
          <p class="text-xs text-gray-400">CompTIA &mdash; Aug 2024</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-certificate text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.credly.com/badges/7b2dc361-956a-4b86-9183-c97e79ba86df/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">CompTIA Network+</a>
          <p class="text-xs text-gray-400">CompTIA &mdash; Feb 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fab fa-aws text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.credly.com/badges/4a875e12-e704-44f6-ada2-2d4da054940a/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">AWS Solutions Architect &mdash; Associate</a>
          <p class="text-xs text-gray-400">AWS &mdash; Mar 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fab fa-google text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.credly.com/badges/a6f69889-6761-4f9f-863e-5ece76672887/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Google Professional Cloud Security Engineer</a>
          <p class="text-xs text-gray-400">Google &mdash; Apr 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-certificate text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://academy.hackthebox.com/achievement/badge/7d790823-39c5-11f0-bcfd-bea50ffe6cb4" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">HTB &amp; Google AI Red Teamer</a>
          <p class="text-xs text-gray-400">HackTheBox + Google &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fab fa-microsoft text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://learn.microsoft.com/api/credentials/share/en-us/Ken-8675/7004E3A174DCBC1D" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Microsoft Azure Fundamentals (AZ-900)</a>
          <p class="text-xs text-gray-400">Microsoft &mdash; Mar 2025</p>
        </div>
      </div>

    </div>

    <!-- Expandable: the rest -->
    <details class="bg-custom-dark/60 border border-gray-700/50 rounded-lg max-w-5xl mx-auto">
      <summary class="flex items-center justify-between px-5 py-4 hover:bg-gray-800/40 transition rounded-lg">
        <span class="font-medium text-blue-200">Show all certifications</span>
        <i class="fas fa-chevron-down text-blue-300 summary-chevron" aria-hidden="true"></i>
      </summary>
      <div class="px-5 pb-6 pt-2">
        <div class="grid md:grid-cols-3 gap-4">

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fab fa-aws text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.credly.com/badges/7ff0fb85-8968-424d-8111-a864dbaeee4d" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">AWS Certified Cloud Practitioner</a>
              <p class="text-xs text-gray-400">AWS &mdash; Mar 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fab fa-google text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.credly.com/badges/3079f837-cb68-4e9f-bb6f-c26f72dc0361/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Google Cloud Digital Leader</a>
              <p class="text-xs text-gray-400">Google &mdash; Apr 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-certificate text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.credly.com/badges/8d1a93d5-9687-49e5-b696-75d48a3cf137/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Google IT Support Professional</a>
              <p class="text-xs text-gray-400">Google &mdash; Nov 2023</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-shield-halved text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.credly.com/badges/00809779-7a33-4262-b2f9-a7b05cbf3e0e/linked_in_profile" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Fortinet Certified Associate in Cybersecurity</a>
              <p class="text-xs text-gray-400">Fortinet &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-shield-halved text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.credly.com/badges/6704d2b6-1127-4a8b-845f-2215f1c3f097/public_url" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Fortinet FortiGate 7.4 Operator</a>
              <p class="text-xs text-gray-400">Fortinet &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-shield-halved text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.credly.com/badges/05b29a42-1fa5-4b3e-9920-488e062e615e/linked_in_profile" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Fortinet Certified Fundamentals in Cybersecurity</a>
              <p class="text-xs text-gray-400">Fortinet &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-lock text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.coursera.org/account/accomplishments/verify/HXSKXK48WM1W" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Blockchain Security</a>
              <p class="text-xs text-gray-400">Infosec &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-robot text-blue-300" aria-hidden="true"></i></div>
            <div>
              <span class="font-bold text-blue-300">AI Security</span>
              <p class="text-xs text-gray-400">Infosec &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-brain text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://coursera.org/share/0358918c5d756b35545f7b33d6cdee81" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">IBM AI Engineering Professional</a>
              <p class="text-xs text-gray-400">IBM &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-brain text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://coursera.org/share/01b1ce0ead8d747e881a45fcfef14e01" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">IBM Generative AI for Cybersecurity</a>
              <p class="text-xs text-gray-400">IBM &mdash; Apr 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-microchip text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.coursera.org/learn/ai-infrastructure-operations-fundamentals/home/module/1" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">AI Infrastructure and Operations</a>
              <p class="text-xs text-gray-400">NVIDIA &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-database text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://credentials.databricks.com/37b1543e-a0c1-4f32-b533-eb7d012ba0ec#acc.qgLw23W0" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Databricks Fundamentals Certified</a>
              <p class="text-xs text-gray-400">Databricks &mdash; Apr 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-database text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://credentials.databricks.com/48957d18-cf66-4caa-90ce-e000f44d0849#acc.axTm38cB" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Databricks Generative AI Fundamentals</a>
              <p class="text-xs text-gray-400">Databricks &mdash; Apr 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-infinity text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.scrumstudy.com/certification/verify?type=SFC&number=1077347" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Scrum Fundamentals Certified (SFC)</a>
              <p class="text-xs text-gray-400">SCRUMstudy &mdash; Apr 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-infinity text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.scrumstudy.com/certification/verify?type=SODFC&number=1014459" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Scrum for Ops &amp; DevOps (SODFC)</a>
              <p class="text-xs text-gray-400">SCRUMstudy &mdash; Apr 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fab fa-jira text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.coursera.org/account/accomplishments/records/IHR5BON1QYHH" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Agile with Atlassian Jira</a>
              <p class="text-xs text-gray-400">Atlassian &mdash; May 2025</p>
            </div>
          </div>

          <div class="panel-card p-5 rounded-lg flex items-start">
            <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-infinity text-blue-300" aria-hidden="true"></i></div>
            <div>
              <a href="https://www.skillfront.com/Badges/48775715319912" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Certified Associate in Scrum Fundamentals (CASF)</a>
              <p class="text-xs text-gray-400">SkillFront &mdash; Apr 2025</p>
            </div>
          </div>

        </div>
      </div>
    </details>

  </div>
</section>

<!-- Education -->
<section id="education" class="py-20 px-6 bg-custom-dark">
  <div class="container mx-auto">
    <p class="section-eyebrow mb-2 text-center">Coursework &amp; Programs</p>
    <h2 class="text-3xl md:text-4xl font-bold mb-12 text-center">Education</h2>
    <div class="grid md:grid-cols-3 gap-4">

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.coursera.org/account/accomplishments/verify/NLFGKEQVGM3Q" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">AI Strategy and Governance</a>
          <p class="text-xs text-gray-400">The Wharton School, UPenn &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.coursera.org/learn/cloud-computing-security/home/welcome" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Advanced System Security Design &mdash; CS 6910</a>
          <p class="text-xs text-gray-400">University of Colorado, Colorado Springs &mdash; June 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://coursera.org/share/5bac352fbd57a3858721b658b0888097" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Continuous Delivery &amp; DevOps</a>
          <p class="text-xs text-gray-400">Darden School of Business, UVA &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://coursera.org/share/5bac352fbd57a3858721b658b0888097" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">DevOps, DataOps, MLOps</a>
          <p class="text-xs text-gray-400">Duke University &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.coursera.org/learn/introduction-to-ai-for-cybersecurity/home/module/1" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Intro to AI for Cybersecurity</a>
          <p class="text-xs text-gray-400">Whiting School of Engineering, JHU &mdash; June 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://www.coursera.org/account/accomplishments/verify/F788WRP5VP3W" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Introduction to DevSecOps</a>
          <p class="text-xs text-gray-400">Whiting School of Engineering, JHU &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://coursera.org/share/63d78b07f81af5e5c2658e982feacb82" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">DevOps Culture and Mindset</a>
          <p class="text-xs text-gray-400">UC Davis &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <a href="https://certificates.mooc.fi/validate/gnpnd8kzcpi" target="_blank" rel="noopener" class="font-bold text-blue-300 hover:underline">Elements of AI</a>
          <p class="text-xs text-gray-400">University of Helsinki &mdash; May 2025</p>
        </div>
      </div>

      <div class="panel-card p-5 rounded-lg flex items-start">
        <div class="bg-blue-900/60 p-3 rounded-full mr-4"><i class="fas fa-university text-blue-300" aria-hidden="true"></i></div>
        <div>
          <span class="font-bold text-blue-300">DevOps with Kubernetes</span>
          <p class="text-xs text-gray-400">University of Helsinki &mdash; Apr 2025</p>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- Contact Section -->
<section id="contact" class="py-20 px-6">
  <div class="container mx-auto text-center max-w-2xl">
    <p class="section-eyebrow mb-2">Get in touch</p>
    <h2 class="text-3xl md:text-4xl font-bold mb-6">Let's connect</h2>
    <p class="text-gray-300 mb-8">Open to remote and hybrid security engineering roles &mdash; particularly where cloud, DevSecOps, and automation intersect.</p>
    <div class="flex flex-wrap justify-center gap-4">
      <a href="mailto:kenbrigham777@gmail.com" class="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2.5 rounded-md font-medium transition">
        <i class="fas fa-envelope mr-2" aria-hidden="true"></i>kenbrigham777@gmail.com
      </a>
      <a href="https://linkedin.com/in/ken-brigham" target="_blank" rel="noopener" class="border border-blue-400/60 hover:border-blue-300 text-blue-200 px-5 py-2.5 rounded-md font-medium transition">
        <i class="fab fa-linkedin mr-2" aria-hidden="true"></i>LinkedIn
      </a>
      <a href="https://github.com/KenB773" target="_blank" rel="noopener" class="border border-gray-600 hover:border-gray-400 text-gray-200 px-5 py-2.5 rounded-md font-medium transition">
        <i class="fab fa-github mr-2" aria-hidden="true"></i>GitHub
      </a>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="cyber-gradient py-6 px-6">
  <div class="container mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
    <div class="flex items-center space-x-2">
      <i class="fas fa-shield-halved text-blue-400 text-xl" aria-hidden="true"></i>
      <span class="text-lg font-bold">Ken Brigham</span>
    </div>
    <p class="text-sm text-blue-200">&copy; 2025 Ken Brigham. All rights reserved.</p>
  </div>
</footer>

</body>
</html>
