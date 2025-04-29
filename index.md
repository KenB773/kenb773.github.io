<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ken Brigham | Cybersecurity, Cloud, AI</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    .cyber-gradient {
      background: linear-gradient(135deg, #1c1c1c 0%, #1b1b1b 50%, #1a1a1a 100%);
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
      <p class="text-xl text-blue-200 mb-8">Cybersecurity | Cloud Operations & Security | Dev(Sec)Ops Engineer | AI/ML Ops</p>
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
          <p class="response mb-4">Threat Intelligence | Cloud Security | DevSecOps | ML Ops</p>
          <p><span class="command">$ contact --method=email</span></p>
          <p class="response">kenbrigham777@gmail.com</p>
          <p><span class="command">$ _</span><span class="cursor"></span></p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Projects Section -->
<section id="projects" class="py-20 px-6 bg-gray-800">
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
        <p class="mb-4">A 3-tier Node.js app deployed to AWS Fargate, RDS, ALB, and provisioned by Terraform, with Docker containerization and SSL security.</p>
        <a href="3TierWebAppProj.md" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">KubeCart Project</h3>
        <p class="mb-4">A containerized Flask microservice deployed on EKS Kubernetes with a live Swagger UI for API interaction.</p>
        <a href="KubeCartProj.md" class="text-blue-400 hover:underline">View Details</a>
      </div>
      <div class="bg-gray-900 rounded-xl overflow-hidden card-hover p-6">
        <h3 class="text-xl font-bold mb-2">Security Scan CI/CD Pipeline</h3>
        <p class="mb-4">GitHub Actions pipeline integrating Trivy, Checkov, Bandit, and OWASP Dependency-Check with SARIF reporting for GitHub Security.</p>
        <a href="https://github.com/KenB773/SecurityScanPipeline" class="text-blue-400 hover:underline">View Project</a>
      </div>
      <!-- Add more projects similarly -->
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
