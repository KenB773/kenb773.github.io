
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ken Brigham | Cyber + Cloud Security, Dev(Sec)Ops, AI/ML Enthusiast</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    .cyber-gradient {
      background: linear-gradient(135deg, #1b1b1c 0%, #1b1b1b 50%, #1a1a1a 100%);
    }
    .neon-text {
      text-shadow: 0 0 5px #3b82f6, 0 0 10px #3b82f6;
    }
    .card-hover { transition: all 0.3s ease; }
    .card-hover:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3); }
    .terminal { background-color: #0f172a; border-radius: 8px; font-family: 'Courier New', monospace; }
    .terminal-header { background-color: #1e293b; border-top-left-radius: 8px; border-top-right-radius: 8px; padding: 8px 15px; }
    .terminal-dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 6px; }
    .terminal-content { padding: 20px; color: #e2e8f0; font-size: 14px; line-height: 1.6; }
    .command { color: #10b981; }
    .response { color: #e2e8f0; }
    .cursor { display: inline-block; width: 10px; height: 18px; background-color: #e2e8f0; animation: blink 1s infinite; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    .hexagon {
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  }
  .bg-custom-dark {
    background-color: #1b1b1b;
  </style>
</head>
<body class="bg-gray-900 text-gray-100 font-sans">

<!-- Navigation -->
<nav class="cyber-gradient py-4 px-6 sticky top-0 z-50 shadow-lg">
  <div class="container mx-auto flex justify-between items-center">
    <div class="flex items-center space-x-2">
      <i class="fas fa-shield-halved text-blue-400 text-2xl"></i>
      <span class="text-xl font-bold">Ken Brigham</span>
    </div>
    <div class="hidden md:flex space-x-8">
      <a href="#projects" class="hover:text-blue-300 transition">Projects</a>
      <a href="#contact" class="hover:text-blue-300 transition">Contact</a>
    </div>
  </div>
</nav>

<!-- Hero Section -->
<section class="cyber-gradient py-20 px-6">
  <div class="container mx-auto flex flex-col md:flex-row items-center">
    <div class="md:w-1/2 mb-10 md:mb-0">
      <h1 class="text-4xl md:text-5xl font-bold mb-4 neon-text">Building & Securing a Cloud-Enabled, AI-Powered Future</h1>
      <p class="text-xl text-blue-200 mb-8">Cybersecurity Analyst | Cloud Security Engineer | Dev(Sec)Ops Engineer | AI/ML Security & Integration</p>
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
          <p class="response mb-4">Ken Brigham - Cyber & Cloud Security Specialist</p>
          <p><span class="command">$ skills --cybersec --cloudsec --devops --aiops</span></p>
          <p class="response mb-4">Cybersecurity | Cloud Security & Engineering | Dev(Sec)Ops | AI/ML</p>
          <p><span class="command">$ contact --method=email</span></p>
          <p class="response">kenbrigham777@gmail.com</p>
          <p><span class="command">$ _</span><span class="cursor"></span></p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Certifications Section -->
<section id="certifications" class="py-20 px-6 bg-custom-dark">
  <div class="container mx-auto">
    <h2 class="text-3xl font-bold mb-12 text-center">Certifications</h2>
    <div class="grid md:grid-cols-3 gap-6">

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/ba475443-2a41-4c31-8874-bc547b68f85b/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">CompTIA Security+</a>
          <p class="text-sm text-gray-400">CompTIA - Aug 2024</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/7b2dc361-956a-4b86-9183-c97e79ba86df/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">CompTIA Network+</a>
          <p class="text-sm text-gray-400">CompTIA - Feb 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/a6f69889-6761-4f9f-863e-5ece76672887/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">Google Professional Cloud Security Engineer (PCSE)</a>
          <p class="text-sm text-gray-400">Google - Apr 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://learn.microsoft.com/api/credentials/share/en-us/Ken-8675/7004E3A174DCBC1D" target="_blank" class="font-bold text-blue-300 hover:underline">Microsoft Certified: Azure Fundamentals (AZ-900)</a>
          <p class="text-sm text-gray-400">Microsoft - Mar 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/4a875e12-e704-44f6-ada2-2d4da054940a/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">AWS Certified Solutions Architect – Associate (SAA)</a>
          <p class="text-sm text-gray-400">AWS - Mar 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/7ff0fb85-8968-424d-8111-a864dbaeee4d" target="_blank" class="font-bold text-blue-300 hover:underline">AWS Certified Cloud Practitioner</a>
          <p class="text-sm text-gray-400">AWS - Mar 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://coursera.org/share/0358918c5d756b35545f7b33d6cdee81" target="_blank" class="font-bold text-blue-300 hover:underline">IBM AI Engineering Professional</a>
          <p class="text-sm text-gray-400">IBM - May 2025</p>
        </div>
      </div>
      
      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://academy.hackthebox.com/achievement/badge/7d790823-39c5-11f0-bcfd-bea50ffe6cb4" target="_blank" class="font-bold text-blue-300 hover:underline">HTB & Google AI Red Teamer</a>
          <p class="text-sm text-gray-400">HackTheBox and Google - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/8d1a93d5-9687-49e5-b696-75d48a3cf137/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">Google IT Support Professional Certificate</a>
          <p class="text-sm text-gray-400">Google - Nov 2023</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/3079f837-cb68-4e9f-bb6f-c26f72dc0361/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">Google Cloud Digital Leader</a>
          <p class="text-sm text-gray-400">Google - Apr 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://coursera.org/share/01b1ce0ead8d747e881a45fcfef14e01" target="_blank" class="font-bold text-blue-300 hover:underline">IBM Generative AI for Cybersecurity Professionals</a>
          <p class="text-sm text-gray-400">IBM - Apr 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.coursera.org/learn/ai-infrastructure-operations-fundamentals/home/module/1" target="_blank" class="font-bold text-blue-300 hover:underline">AI Infrastructure and Operations</a>
          <p class="text-sm text-gray-400">NVIDIA - May 2025</p>
        </div>
      </div>      

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/00809779-7a33-4262-b2f9-a7b05cbf3e0e/linked_in_profile" target="_blank" class="font-bold text-blue-300 hover:underline">Fortinet Certified Associate in Cybersecurity</a>
          <p class="text-sm text-gray-400">Fortinet - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/6704d2b6-1127-4a8b-845f-2215f1c3f097/public_url" target="_blank" class="font-bold text-blue-300 hover:underline">Fortinet FortiGate 7.4 Operator</a>
          <p class="text-sm text-gray-400">Fortinet - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.credly.com/badges/05b29a42-1fa5-4b3e-9920-488e062e615e/linked_in_profile" target="_blank" class="font-bold text-blue-300 hover:underline">Fortinet Certified Fundamentals in Cybersecurity</a>
          <p class="text-sm text-gray-400">Fortinet - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.scrumstudy.com/certification/verify?type=SFC&number=1077347" target="_blank" class="font-bold text-blue-300 hover:underline">Scrum Fundamentals Certified (SFC)</a>
          <p class="text-sm text-gray-400">SCRUMstudy - Apr 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.scrumstudy.com/certification/verify?type=SODFC&number=1014459" target="_blank" class="font-bold text-blue-300 hover:underline">Scrum for Ops and DevOps Fundamentals Certified (SODFC)</a>
          <p class="text-sm text-gray-400">SCRUMstudy - Apr 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.coursera.org/account/accomplishments/records/IHR5BON1QYHH" target="_blank" class="font-bold text-blue-300 hover:underline">Agile with Atlassian Jira</a>
          <p class="text-sm text-gray-400">Atlassian - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.coursera.org/account/accomplishments/verify/HXSKXK48WM1W" target="_blank" class="font-bold text-blue-300 hover:underline">Blockchain Security</a>
          <p class="text-sm text-gray-400">Infosec - May 2025</p>
        </div>
      </div>
      
      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://kenb773.github.io/" target="_blank" class="font-bold text-blue-300 hover:underline">AI Security</a>
          <p class="text-sm text-gray-400">Infosec - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://credentials.databricks.com/37b1543e-a0c1-4f32-b533-eb7d012ba0ec#acc.qgLw23W0" target="_blank" class="font-bold text-blue-300 hover:underline">Databricks Fundamentals Certified</a>
          <p class="text-sm text-gray-400">Databricks - Apr 2025</p>
        </div>
      </div>      
      
      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://credentials.databricks.com/48957d18-cf66-4caa-90ce-e000f44d0849#acc.axTm38cB" target="_blank" class="font-bold text-blue-300 hover:underline">Databricks Generative AI Fundamentals</a>
          <p class="text-sm text-gray-400">Databricks - Apr 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-certificate text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.skillfront.com/Badges/48775715319912" target="_blank" class="font-bold text-blue-300 hover:underline">Certified Associate in Scrum Fundamentals (CASF)</a>
          <p class="text-sm text-gray-400">SkillFront - Apr 2025</p>
        </div>
      </div>

    </div>
  </div>
</section>

<section id="education" class="py-20 px-6 bg-custom-dark">
  <div class="container mx-auto">
    <h2 class="text-3xl font-bold mb-12 text-center">Education</h2>
    <div class="grid md:grid-cols-3 gap-6">

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.coursera.org/account/accomplishments/verify/NLFGKEQVGM3Q" target="_blank" class="font-bold text-blue-300 hover:underline">
           AI Strategy and Governance
          </a>
          <p class="text-sm text-gray-400">The Wharton School, University of Pennsylvania - May 2025</p>
        </div>
      </div>      

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.coursera.org/learn/cloud-computing-security/home/welcome" target="_blank" class="font-bold text-blue-300 hover:underline">
           Advanced System Security Design Specialization - CS 6910
          </a>
          <p class="text-sm text-gray-400">University of Colorado, Colorado Springs- June 2025</p>
        </div>
      </div>
      
      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://coursera.org/share/5bac352fbd57a3858721b658b0888097" target="_blank" class="font-bold text-blue-300 hover:underline">
            DevOps, DataOps, MLOps
          </a>
          <p class="text-sm text-gray-400">Duke University - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://www.coursera.org/learn/introduction-to-ai-for-cybersecurity/home/module/1" target="_blank" class="font-bold text-blue-300 hover:underline">
            Introduction to Artificial Intelligence for Cybersecurity
          </a>
          <p class="text-sm text-gray-400">Whiting School of Engineering, Johns Hopkins University - June 2025</p>
        </div>
      </div>      

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="#" target="_blank" class="font-bold text-blue-300 hover:underline">
            Introduction to DevSecOps
          </a>
          <p class="text-sm text-gray-400">Whiting School of Engineering, Johns Hopkins University - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://coursera.org/share/63d78b07f81af5e5c2658e982feacb82" target="_blank" class="font-bold text-blue-300 hover:underline">
            DevOps Culture and Mindset
          </a>
          <p class="text-sm text-gray-400">University of California, Davis - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="https://certificates.mooc.fi/validate/gnpnd8kzcpi" target="_blank" class="font-bold text-blue-300 hover:underline">
            Elements of AI
          </a>
          <p class="text-sm text-gray-400">University of Helsinki - May 2025</p>
        </div>
      </div>

      <div class="bg-gray-800 p-6 rounded-lg flex items-start">
        <div class="bg-blue-900 p-3 rounded-full mr-4">
          <i class="fas fa-university text-blue-300 text-xl"></i>
        </div>
        <div>
          <a href="#" target="_blank" class="font-bold text-blue-300 hover:underline">
            DevOps with Kubernetes
          </a>
          <p class="text-sm text-gray-400">University of Helsinki - Apr 2025</p>
        </div>
      </div>

    </div>
  </div>
</section>



<!-- Projects Section -->
<section id="projects" class="py-20 px-6 bg-custom-dark">
  <div class="container mx-auto">
    <h2 class="text-3xl font-bold mb-12 text-center">Projects</h2>
    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">Quick Incident Triage Toolkit</h3>
        <p class="mb-4">A sleek offline desktop app built with Rust, Tauri, and React for rapid system diagnostics with real-time monitoring and JSON export.</p>
        <a href="https://github.com/KenB773/QuickIncidentTriageToolkit" class="text-blue-400 hover:underline">View Project</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">AWS 3-Tier Web App</h3>
        <p class="mb-4">A 3-tier Node.js app deployed to AWS Fargate incorporating PostgreSQL and ALB, provisioned by Terraform with Docker containerization.</p>
        <a href="https://github.com/KenB773/3TierWebAppTerraform" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">AWS IaC Drift Detector</h3>
        <p class="mb-4">A Go-based CLI tool that detects configuration drift between Terraform-managed infrastructure and the actual state of AWS resources.</p>
        <a href="3TierWebAppProj.md" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">OpenAI Chatbot UI with Jenkins/AWS EKS</h3>
        <p class="mb-4"> OpenAI Chatbot UI deployed with Jenkins, EKS and Terraform - built with DevSecOps in mind.</p>
        <a href="https://github.com/KenB773/ChatbotUIJenkins" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">Azure DevOps Pipeline</h3>
        <p class="mb-4">Terraform deployments at scale using Azure DevOps, Service Principals, and secure CI/CD pipelines.</p>
        <a href="https://github.com/KenB773/AzureDevOpsPipeline" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">AWS/GCP KubeCart Project</h3>
        <p class="mb-4">A containerized Flask microservice deployed on EKS Kubernetes with a live Swagger UI for API interaction.</p>
        <a href="https://github.com/KenB773/KubeCart" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">Security Scan CI/CD Pipeline</h3>
        <p class="mb-4">GitHub Actions pipeline integrating Trivy, Checkov, Bandit, and OWASP Dependency-Check with SARIF reporting for GitHub Security.</p>
        <a href="https://github.com/KenB773/SecurityScanPipeline" class="text-blue-400 hover:underline">View Project</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">Home SOC on Azure</h3>
        <p class="mb-4">Functional personal SOC using Azure Monitor, Log Analytics, and Sentinel to track simulated home network threats in real time.</p>
        <a href="homesoc.html" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">'RogueSpeared' Tool</h3>
        <p class="mb-4">Red-team PoC that creates polyglot WAV+Python files that play audio but execute encrypted payloads when run as scripts.</p>
        <a href="https://github.com/KenB773/RogueSpeared" class="text-blue-400 hover:underline">View Project</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">AWS PartyRock: JargonBridge</h3>
        <p class="mb-4">An LLM-powered app that explains technical jargon in plain English and vice versa using Amazon PartyRock.</p>
        <a href="https://partyrock.aws/u/KenB7/1nIRFrtOV/JargonBridge" class="text-blue-400 hover:underline">View App</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">AWS Silent Scalper</h3>
        <p class="mb-4">Serverless AWS pipeline that triggers processing on file upload and autoscaling, eliminating idle compute time.</p>
        <a href="smart-vault.html" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">AWS Smart Vault</h3>
        <p class="mb-4">Backup management tool for EBS snapshots using EventBridge and Lambda. Features audit logs and cleanup automation.</p>
        <a href="smart-vault.html" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">TryHackMe SOC Level 1</h3>
        <p class="mb-4">Blue-team training and lab walkthroughs from the TryHackMe SOC Level 1 course.</p>
        <a href="thmsoclevel1.html" class="text-blue-400 hover:underline">View Notes</a>
      </div>
    </div>
  </div>
</section>

<!-- Contact Section -->
<section id="contact" class="py-20 px-6 bg-gray-900">
  <div class="container mx-auto text-center">
    <h2 class="text-3xl font-bold mb-12">Contact</h2>
    <p>Email me at <span class="text-blue-400">kenbrigham777@gmail.com</span> or connect on <a href="https://linkedin.com/in/ken-brigham" class="text-blue-400 hover:underline">LinkedIn</a>.</p>
  </div>
</section>

<!-- Footer -->
<footer class="cyber-gradient py-6 px-6">
  <div class="container mx-auto flex justify-between items-center">
    <div class="flex items-center space-x-2">
      <i class="fas fa-shield-halved text-blue-400 text-xl"></i>
      <span class="text-lg font-bold">Ken Brigham</span>
    </div>
    <p class="text-sm text-blue-200">&copy; 2025 Ken Brigham. All rights reserved.</p>
  </div>
</footer>

</body>
</html>
