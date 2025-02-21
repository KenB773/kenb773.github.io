---
layout: default
---

Thanks for visiting my portfolio! What will follow is a rough outline of the various aspects of my hands-on learning & experience in the realm of cyberecurity - this **is not meant to be comprehensive**, but rather to highlight & quantify some of the tangible skills and techniques that I've practiced. 
I currently hold, among others, active Security+ and Network+ certifications from CompTIA (which hopefully verify at least some level of foundational knowledge), so the projects here will likely be more technical and role-specific as opposed to generalized knowledge. 


# TryHackMe - SOC Level 1

![THM SOCL1 Icon](TryHackMe SOC L1 Icon.png)

The first role-specific labs I'll be documenting will come from TryHackMe's SOC Level 1 learning path & certificate! 

## Module 1. Intro

Right off the bat and from the very first module, they have us using a simplified, mock SIEM to identify a malicious connection attempt, use a mock open-source IP address database to determine if the IP is known to be malicious, escalate the alert to the correct team member (in this case, the SOC Team Lead) and then block the IP address in the firewall once given permission to do so.

See photos below:

![SIEM](TryHackMe SIEM 1.png)

![IP Check](TryHackMe OS Database IP Checking 1.png)

And the questions + answers:

![Q+A](THM Module 1 Q+A.png)


## Module 2. Pyramid of Pain

Next up is the Pyramid of Pain - this is essentially a framework that demonstrates how certain IoCs are more troubling to a threat actor than another, and is used to enhance Cyber Threat Intelligence (CTI) in many cybersecurity solutions. From AttackIQ: "The Pyramid of Pain ... provides an ascending priority list of indicators against which security controls should be applied." So, starting from the bottom and working up:

### Trivial - Hash Values

Hash values are exceptionally easy for a threat actor to circumvent, as modifying a file by even a single bit and then recompiling will produce a different hash and therefore entirely sidestep an attempted control at this level. See below for given example:

![Hash Example](THM Mod 2 - Hash.png)

### Easy - IP Address

IP addresses are also quite easy for even less experienced adversaries to work around. Blocking or denying inbound traffic/requests from a given IP is not a bulletproof defense, despite being a common (and still useful) defense tactic. We are then given an example of how threat actors can work around a control at this level, and provided static reports from [any.run](https://any.run/) to analyze and then answer the following:

![IP Example](THM Mod 2 - IP + FastFlux.png)

### Simple - Domain Names

Moving up the Pyramid once again, we have domain names. Direct from THM: "Domain Names can be a little more of a pain for the attacker to change as they would most likely need to purchase the domain, register it and modify DNS records. Unfortunately for defenders, many DNS providers have loose standards and provide APIs to make it even easier for the attacker to change the domain."

![Domain Sodinokibi C2s](THM Sodinokibi C2 domains.png)

![Domain Punycode Example](THM Mod 2 - Domain Punycode.png)

The module goes on to explain the use of URL shorteners, and how they are commonly used to hide malicious domain names, and provides a potential negation tactic in appending a '+' to the shortened URL to see the full domain you are being directed to. For example, "http://bit.ly/275hf9**+**" would show the actual destination of that link. Next, we circle back to the ever-so-useful any.run. Being a sandboxing service that executes a sample, it allows us to review connections such as HTTP or DNS requests, or see any processes attempting to communicate with an external IP. 

Finally, we're given an actual sandboxed file on AnyRun, and asked to answer the following questions by analzying the information in the pictured report:

![Sandbox AnyRun](THM Mod 2 AnyRun Sandbox.png)


![THM Mod 2 Q+A](THM Mod 2 - Q + A.png)

### Annoying - Host Artifacts

Moving up another step into the 'yellow zone', we have host artifacts. This is where the attacker will begin to feel much more frustrated if the attack is detected as it would likely require them to change their tools and methodologies, which can be very time consuming.

From THM: "Host artifacts are the traces or observables that attackers leave on the system, such as registry values, suspicious process execution[s], attack patterns or IOCs (Indicators of Compromise), files dropped by malicious applications, or anything exclusive to the current threat."

![Host Artifact Sus Proc Execution](THM Mod 2 - Host Artifiacts Sus Events.png)

![Host Artifacts Dropped Files](THM Mod 2 - HA Dropped Files.png)

We are then given an [example malware analysis report](https://assets.tryhackme.com/additional/pyramidofpain/task5-report.pdf), and asked to answer several questions based on the information within it:

![HA Q+A](THM Mod 2 - HA Q+A.png)

### Annoying - Network Artifacts

In the same 'yellow zone' as Host Artifacts are Network Artifacts. Again from THM: "A network artifact can be a user-agent string, C2 information, or URI patterns followed by the HTTP POST requests. An attacker might use a User-Agent string that hasn’t been observed in your environment before or seems out of the ordinary. The User-Agent is defined by RFC2616 as the request-header field that contains the information about the user agent originating the request."

We're given some background and explanations here, as well as the first mention of our dearly beloved Wireshark!

![NA Def](THM Mod 2 - Network Artifacts.png)

Then some questions regarding the above screenshots:

![NA Q+A](THM Mod 2 - NA Q+A.png)

### Challenging - Tools

At this point in the Pyramid, an attacker will likely give up, or if they're sufficiently advanced and/or committed, will at least have to go back to the drawing board and create a new tool that serves the same purpose. Threat actors without sufficient resources to continue will often be deflected at this point.

![TMH Tools](THM Mod 2 - Tools.png)

We get a description of fuzzy hashing and similarity analysis, as well as some info on SSDEEP and an example report from VirusTotal which highlights the SSDEEP. Some questions follow, which mostly involve SSDEEP's official website and their descriptions of terminology within.

### Tough - TTPs

We finally reach the apex of the Pyramid of Pain, where we have Tactics, Techniques & Procedures. We get our first mention of the omnipresent MITRE ATT&CK Matrix, which is a framework that lists, essentially, all the steps taken by a cyber adversary to achieve their goal in almost any possible circumstance. By detecting and responding to TTPs quickly, we leave the threat actor almost no chance to fight back.

The questions we are given primarily relate to navigating and finding specific information within the ATT&CK framework, which has become something of a part-time job for me at this point! The edutainment on offer is truly bottomless.


### Pyramid of Pain - Practical

The practical involves matching descriptions to each 'block' of the Pyramid, then entering the flag awarded for doing so.

### Pyramid of Pain - Conclusion

We finished the module!

![Module 2 Conclusion](THM Mod 2 - Conclusion.png)

## Module 3 - Cyber Kill Chain

![CyberKillChain](THM Cyber Kill Chain.png)

Moving on to the next module - Cyber Kill Chain! In the words of THM:

"The term kill chain is a military concept related to the structure of an attack. It consists of target identification, decision and order to attack the target, and finally the target destruction.

Thanks to Lockheed Martin, a global security and aerospace company, that established the Cyber Kill Chain® framework for the cybersecurity industry in 2011 based on the military concept. The framework defines the steps used by adversaries or malicious actors in cyberspace. To succeed, an adversary needs to go through all phases of the Kill Chain. We will go through the attack phases and help you better understand adversaries and their techniques used in the attack to defend yourself.

So, why is it important to understand how Cyber Kill Chain works? 

The Cyber Kill Chain will help you understand and protect against ransomware attacks, security breaches as well as Advanced Persistent Threats (APTs). You can use the Cyber Kill Chain to assess your network and system security by identifying missing security controls and closing certain security gaps based on your company's infrastructure.

By understanding the Kill Chain as a SOC Analyst, Security Researcher, Threat Hunter, or Incident Responder, you will be able to recognize the intrusion attempts and understand the intruder's goals and objectives. 

We will be exploring the following attack phases in this room:

1. Reconnaissance
2. Weaponization
3. Delivery
4. Exploitation
5. Installation
6. Command & Control
7. Actions on Objectives 

Learning Objectives: In this room, you will learn about each phase of the Cyber Kill Chain Framework, the advantages and disadvantages of the traditional Cyber Kill Chain. 

Outcome: As a result, you will be ready to recognize different phases or stages of the attack carried out by an adversary and be able to break the "kill chain.""

### Reconnaissance 

The topic of OSINT is introduced, and specifically email harvesting is focused on with various examples of tools used, such as [theHarvester](https://github.com/laramies/theHarvester) here on Github.

### Weaponization

After a succesful reconnaissance stage, the threat actor will combine **malware** and **exploit(s)** into a deliverable **payload**. Malware may be custom-written by threat actors with access to more advanced resources, or can be software-generated or simply purchased on dark web markets. Per THM:

"**Malware** is a program or software that is designed to damage, disrupt, or gain unauthorized access to a computer.

An **exploit** is a program or a code that takes advantage of the vulnerability or flaw in the application or system.

A **payload** is a malicious code that the attacker runs on the system."

### Delivery

Delivery is when the threat actor decides on the method for distributing their payload or malware. Common options include phishing emails, distributing infected USB drives (with various degrees of sophistication) and watering hole attacks, but there are many more that exist besides these.

### Exploitation 

To gain access to a system, the attacker must then exploit the vulnerability. The concept of lateral movement is introduced and defined, as well as the first mention of the OWASP TOP 10 and the link to a TryHackMe room in which all 10 are discussed and exploited in real-time labs (will do and document this at a later date). Zero-day exploits are also introduced and talked about.

### Installation

Per THM: "Once the attacker gets access to the system, he would want to reaccess the system if he loses connection to it or if he gets detected and has the initial access removed, or if the system is later patched. That is when the attacker needs to install a persistent backdoor. A persistent backdoor will let the attacker access the system he compromised in the past."

Persistence can be achieved through web shells, installed backdoors via programs such as Meterpreter, [creating/modifying Windows services](https://attack.mitre.org/techniques/T1543/003/), or by adding the entry to the "run keys" for the malicious payload in the Registry or the Startup folder. In this phase, the attacker can also use the [Timestomping](https://attack.mitre.org/techniques/T1070/006/) technique to avoid detection by the forensic investigator and also to make the malware appear as a part of a legitimate program. The Timestomping technique lets an attacker modify the file's timestamps, including the modify, access, create and change times. 

### Command & Control (C2)

After gaining persistence and executing the malware on the target machine, the attacker can open a C2 channel through the malware to remotely control and manipulate the victim. This is also written as C&C or C2 Beaconing, and is a type of malicious communication between a C2 server and the malware on an infected host. The compromised endpoint would communicate with an external server set up by the attacker to establish a command & control channel. After establishing this connection, the attacker gains full control of the victim's machine. THM:

"The most common C2 channels used by adversaries nowadays:

The protocols HTTP on port 80 and HTTPS on port 443 - this type of beaconing blends the malicious traffic with the legitimate traffic and can help the attacker evade firewalls.  
DNS (Domain Name Server). The infected machine makes constant DNS requests to the DNS server that belongs to an attacker, this type of C2 communication is also known as DNS Tunneling.
[it is] important to note that [either] an adversary or another compromised host can be the owner of the C2 infrastructure."

### Actions on Objectives (Exfiltration)

After going through the previous 6 phases of the attack, the attacker can finally achieve their goals, which means taking action on their original objectives. With hands-on keyboard access, the attacker can achieve the following: 

*  Collect the credentials from users.
*  Perform privilege escalation (gaining elevated access like domain administrator access from a workstation by exploiting the misconfiguration).
*  Internal reconnaissance (for example, an attacker gets to interact with internal software to find its vulnerabilities).
*  Lateral movement through the company's environment.
*  Collect and exfiltrate sensitive data.
*  Deleting the backups and shadow copies. Shadow Copy is a Microsoft technology that can create backup copies, snapshots of computer files, or volumes. 
*  Overwrite or corrupt data.

### Cyber Kill Chain - Practical

Similar to the previous practical, we are required to match general concepts to the different stages of the Chain.

### Cyber Kill Chain - Conclusion

We have finished the module! THM offers some closing thoughts on the CKC - see below.

![CKC Conclusion](THM Mod 3 - CKC Conclusion.png)


## Module 4 - Unified Kill Chain

THM: "Understanding the behaviours, objectives and methodologies of a cyber threat is a vital step to establishing a strong cybersecurity defence (known as a cybersecurity posture).

In this room, you will be introduced to the UKC (Unified Kill Chain) framework that is used to help understand how cyber attacks occur."

### Threat Modelling

Threat modelling, in a cybersecurity context, is a series of steps to ultimately improve the security of a system. Threat modelling is about identifying risk and essentially boils down to:

*  Identifying what systems and applications need to be secured and what function they serve in the environment. For example, is the system critical to normal operations, and is a system holding sensitive information like payment info or addresses?
*  Assessing what vulnerabilities and weaknesses these systems and applications may have and how they could be potentially exploited
*  Creating a plan of action to secure these systems and applications from the vulnerabilities highlighted
*  Putting in policies to prevent these vulnerabilities from occurring again where possible (for example, implementing a software development life cycle (SDLC) for an application or training employees on phishing awareness).

Threat modelling is an important procedure in reducing the risk within a system or application, as it creates a high-level overview of an organisation's IT assets (an asset in IT is a piece of software or hardware) and the procedures to resolve vulnerabilities.

The UKC can encourage threat modelling as the UKC framework helps identify potential attack surfaces and how these systems may be exploited. STRIDE, DREAD and CVSS (to name a few) are all frameworks specifically used in threat modelling.

### Introducing the UKC

The UKC is more modern & detailed than many other frameworks, and is meant to be used in **complement** to (not in competition with) them.

![UKC Visual](THM Unified Kill Chain.png)


### UKC Phases - In, Through, Out

*  In: Initial Foothold - Recon, Weaponization, Social Engineering, Exploitation, Persistence, Defence Evasion, C2, Pivoting
*  Through: Network Propagation - Pivoting, Disocvery, Privilege Escalation, Execution, Credential Access, Lateral Movement
*  Out: Action on Objectives - Collection, Exfiltration, Impact

### UKC - Practical

Once again, matching TTPs to the phases of the Unified Kill Chain.

### UKC - Conclusion

Another module finished!

![UKC Conclusion](THM Mod 4 - Conclusion.png)


## Module 5 - Diamond Model

We begin Module 5, and are introduced to the Diamond Model!

![Diamond Model](THM Mod 5 - Diamond Model Intro.png)

### Diamond Model 5 - Practical & Conclusion

After several short sections of review with some questions along the way, we create our own Diamond Model on the 2016 Ukrainian Power Grid Attacks, using [this case study](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2016/05/20081514/E-ISAC_SANS_Ukraine_DUC_5.pdf).

## Module 6 - MITRE

Now we get to dive into MITRE and their many, many contributions to the world of cybersecurity! CVEs, ATT&CK, CAR, Engage, D3FEND, AEP and more.

### MITRE - ATT&CK

Per THM:
"What is the ATT&CK® framework? According to the website, "MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations." In 2013, MITRE began to address the need to record and document common TTPs (Tactics, Techniques, and Procedures) that APT (Advanced Persistent Threat) groups used against enterprise Windows networks. This started with an internal project known as FMX (Fort Meade Experiment). Within this project, selected security professionals were tasked to emulated adversarial TTPs against a network, and data was collected from the attacks on this network. The gathered data helped construct the beginning pieces of what we know today as the ATT&CK® framework.

The ATT&CK® framework has grown and expanded throughout the years. One notable expansion was that the framework focused solely on the Windows platform but has expanded to cover other platforms, such as macOS and Linux. The framework is heavily contributed to by many sources, such as security researchers and threat intelligence reports. Note this is not only a tool for blue teamers. The tool is also useful for red teamers."

![ATTCK NAV](THM Mod 6 ATT&CK Nav.png)

We start to use the ATT&CK Framework + Navigator to answer various questions regarding specific groups, their overlap with others, software used by them and its definitions, and techniques attributed to specific APTs.

### MITRE Cyber Analytics Repository (CAR)

We review various pages and learn how to use the analytics provided. CAR Analytics go deeper than Mitigations & Detection in the ATT&CK framework, and therefore is a very useful addition to be used alongside it.

### MITRE Engage Matrix

![MITRE ENGAGE](THM MITRE ENGAGE Matrix.png)

We are introduced to the Engage Matrix. This is considered an Adversary Engagement Approach, and is accomplished by the implementation of Cyber Denial and Cyber Deception. 

*  Prepare the set of operational actions that will lead to your desired outcome (input).
*  Expose adversaries when they trigger your deployed deception activities.
*  Affect adversaries by performing actions that will have a negative impact on their operations.
*  Elicit information by observing the adversary and learn more about their modus operandi (TTPs).
*  Understand the outcomes of the operational actions (output).

![Engage Gif](Engage Matrix Gif.gif)

We engage with Engage (haha) and use the matrix and some tools/worksheets to answer a few questions about it.

### MITRE D3FEND

