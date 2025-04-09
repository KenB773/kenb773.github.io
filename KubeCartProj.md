# KubeCart – Flask Microservice on AWS EKS

**Live Demo:** [http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com](http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com) 
**Swagger Docs:** [http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/swagger](http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/swagger)

**[View the KubeCart Repository](https://github.com/KenB773/KubeCart)**

---

## 📦 Overview

This one was a doozy, as the kids (probably don't) say. A whole lot of debugging dragged the process out for a few extra hours, only to be an odd stale cache bug with a relatively simple fix. All's well that ends well though, and I think this one ended pretty well! **KubeCart** is a simulated shopping cart microservice written in Python with Flask and Flask-RESTX. It’s deployed to AWS using EKS (Elastic Kubernetes Service) and exposed through an internet-facing Load Balancer.

The app demonstrates:
- Cloud-native architecture
- Containerization with Docker
- Infrastructure deployment with `eksctl`
- REST API documentation with Swagger (via `/swagger`)
- Full Kubernetes deployment with public access

---

## 📐 Architecture

```
                     ┌──────────────────────────────┐
                     │   👨‍💻 Local Development       │
                     │------------------------------│
                     │ - Windows 11 + Git Bash       │
                     │ - Flask + Flask-RESTX         │
                     │ - Docker Desktop              │
                     │ - AWS CLI, eksctl, kubectl    │
                     └────────────┬─────────────────┘
                                  │
                                  ▼
         ┌───────────────────────────────────────────┐
         │  Docker Build & Push to Docker Hub        │
         │  Image: kenb773/kubecart:swaggerfix        │
         └────────────┬──────────────────────────────┘
                      │
                      ▼
            ┌───────────────────────────────┐
            │ Amazon EKS (Elastic K8s)      │
            │ Cluster via eksctl            │
            └────────┬───────────────┬──────┘
                     │               │
                     ▼               ▼
       ┌─────────────────┐   ┌─────────────────┐
       │ EC2 Node (Pod 1)│   │ EC2 Node (Pod 2)│
       │ - Flask         │   │ - Flask         │
       │ - RESTX         │   │ - RESTX         │
       │ - /cart         │   │ - /swagger      │
       └─────────────────┘   └─────────────────┘
                     ▲               ▲
                     └────┬────┬─────┘
                          ▼    ▼
            ┌──────────────────────────────┐
            │ Kubernetes Service (LB)      │
            │ - Exposes port 80 → 5000     │
            └────────────┬─────────────────┘
                         ▼
      ┌────────────────────────────────────────────┐
      │ AWS Elastic Load Balancer (ELB - Public IP)│
      └────────────────────────────────────────────┘
                         ▲
                         │
         ┌───────────────┴────────────────┐
         │     🌐 User's Web Browser       │
         │     Accesses /, /swagger, etc. │
         └────────────────────────────────┘
```

---

## 🧠 Key Skills Demonstrated

- Kubernetes deployment via `kubectl` and `eksctl`
- Debugging rollout & image caching issues on EKS
- Live Swagger UI inside container
- Service exposure and load balancer setup on AWS

---

## 🧪 Try It Live

Interact with the app using Swagger UI, Postman, or curl:

```bash
curl http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/cart?user_id=guest
```

