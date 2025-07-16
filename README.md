# Smart-llm-routing


# LLM Load Balancer Inference Architecture

This project demonstrates a scalable and fault-tolerant deployment architecture using AWS services to serve multiple Large Language Models (LLMs) behind a single API endpoint. The setup leverages an **Application Load Balancer (ALB)** to route traffic between **two EC2 instances**, each hosting a different LLM.

---

## 🚀 Features

- 🌐 REST API-based access to LLMs behind a unified endpoint
- ⚖️ Application Load Balancer distributes traffic evenly or conditionally
- 🔐 Secure deployment using AWS Security Groups
- 🧠 Supports model specialization (e.g., general-purpose vs. domain-specific LLMs)
- 📈 High availability with health checks and instance failover

---

## 📦 Tech Stack

- AWS EC2 (LLM Model Deployment)
- AWS ALB (Application Load Balancer)
- Flask / FastAPI (for LLM-serving APIs)
- Python (LLM serving + inference logic)

---

## 🏗️ Architecture

