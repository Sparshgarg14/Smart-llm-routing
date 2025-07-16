# Smart-llm-routing
Do check the images of screenshots for better understanding and also checkout my LinkedIn page for better understanding 
LinkedIn link - https://www.linkedin.com/in/sparsh-garg14/

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

      +----------------------+
      |   Client / API Call  |
      +----------+-----------+
                 |
          +------+------+
          |   Load      |
          |  Balancer   |
          +------+------+
                 |
   +-------------+-------------+
   |                           |
+------v------+ +--------v------+
| EC2: LLM 1 | | EC2: LLM 2 |
| (e.g., GPT)| | (e.g., Mistral)|
+-------------+ +---------------+