# ⚡ NeuralStreamX

<div align="center">

## AI-Powered Real-Time Kafka Streaming Analytics Platform

A futuristic real-time streaming analytics platform built using Apache Kafka, PySpark Streaming, PostgreSQL, Docker, and Streamlit.

Designed to simulate enterprise-grade streaming pipelines with real-time analytics, fraud detection, monitoring, and cyberpunk-style visualization.

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-black?style=for-the-badge&logo=apachekafka)
![PySpark](https://img.shields.io/badge/PySpark-Streaming-orange?style=for-the-badge&logo=apachespark)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)

</div>

---

# 🚀 Features

- ⚡ Real-time Kafka event streaming
- 🔥 PySpark Structured Streaming pipeline
- 🧠 AI-style fraud detection alerts
- 📊 Futuristic live analytics dashboard
- 🌍 Real-time transaction monitoring
- 🐳 Dockerized infrastructure
- 💾 PostgreSQL persistent storage
- 📈 Streaming transformations
- 🛰 Monitoring and logging system
- 🔄 Fault tolerance & checkpointing
- 🎨 Cyberpunk-inspired UI design

---

# 🏗 Enterprise Architecture

```mermaid
flowchart TB

%% =====================================
%% STYLES
%% =====================================

classDef producer fill:#111827,stroke:#00F5FF,color:#ffffff,stroke-width:2px
classDef kafka fill:#1E1B4B,stroke:#8B5CF6,color:#ffffff,stroke-width:2px
classDef processing fill:#0F172A,stroke:#38BDF8,color:#ffffff,stroke-width:2px
classDef storage fill:#052E16,stroke:#22C55E,color:#ffffff,stroke-width:2px
classDef dashboard fill:#3B0764,stroke:#E879F9,color:#ffffff,stroke-width:2px
classDef infra fill:#3F3F46,stroke:#FACC15,color:#ffffff,stroke-width:2px

%% =====================================
%% DATA GENERATION
%% =====================================

subgraph L1["📡 DATA GENERATION"]

    P1["🖥 Producer Service
    Python Kafka Producer"]

end

%% =====================================
%% KAFKA LAYER
%% =====================================

subgraph L2["⚡ EVENT STREAMING"]

    K1["📨 Apache Kafka"]

    K2["📂 Topic
    customer-events"]

end

%% =====================================
%% PROCESSING LAYER
%% =====================================

subgraph L3["🔥 REAL-TIME PROCESSING"]

    S1["⚙ PySpark Streaming"]

    S2["🧠 Transformation Engine"]

    S3["🚨 Fraud Detection Engine"]

end

%% =====================================
%% STORAGE LAYER
%% =====================================

subgraph L4["💾 STORAGE"]

    DB1["🐘 PostgreSQL"]

    DB2["📊 streaming_events"]

end

%% =====================================
%% VISUALIZATION
%% =====================================

subgraph L5["📊 VISUALIZATION"]

    D1["⚡ NeuralStreamX Dashboard"]

    D2["📈 Real-Time Analytics"]

    D3["🛰 Monitoring & Telemetry"]

end

%% =====================================
%% INFRASTRUCTURE
%% =====================================

subgraph L6["🐳 INFRASTRUCTURE"]

    I1["🐳 Docker"]

    I2["📡 Zookeeper"]

    I3["⚡ Kafka Container"]

    I4["🐘 PostgreSQL Container"]

end

%% =====================================
%% FLOW
%% =====================================

P1 --> K1

K1 --> K2

K2 --> S1

S1 --> S2

S2 --> S3

S3 --> DB1

DB1 --> DB2

DB2 --> D1

D1 --> D2

D1 --> D3

%% =====================================
%% INFRA LINKS
%% =====================================

I1 -.-> I2

I1 -.-> I3

I1 -.-> I4

%% =====================================
%% APPLY STYLES
%% =====================================

class P1 producer

class K1,K2 kafka

class S1,S2,S3 processing

class DB1,DB2 storage

class D1,D2,D3 dashboard

class I1,I2,I3,I4 infra
```

---

# 📸 Dashboard Preview

## ⚡ NeuralStreamX Real-Time Dashboard

![Dashboard](screenshots/dashboard.png)

---

# 📊 Dashboard Features

- 📈 Real-time revenue analytics
- 🌍 City-wise transaction monitoring
- 🛒 Product distribution analysis
- 🚨 AI fraud detection alerts
- ⚡ Live activity feed
- 🛰 System health telemetry
- 🎨 Cyberpunk futuristic UI

---

# ⚙ Tech Stack

| Technology | Purpose |
|---|---|
| Apache Kafka | Real-time event streaming |
| PySpark Streaming | Stream processing |
| PostgreSQL | Data persistence |
| Docker | Containerized infrastructure |
| Streamlit | Dashboard visualization |
| Plotly | Interactive charts |
| Python | Backend & streaming logic |

---

# 📂 Project Structure

```bash
real-time-kafka-streaming-pipeline/
│
├── configs/
├── consumer/
├── dashboard/
├── database/
├── docker/
├── docs/
├── logs/
├── monitoring/
├── producer/
├── screenshots/
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🐳 Docker Infrastructure

Containerized services:

- 📡 Apache Kafka
- ⚡ Zookeeper
- 🐘 PostgreSQL

Start all services:

```bash
docker-compose up -d
```

---

# ▶ Running The Project

## 1️⃣ Start Kafka Producer

```bash
python producer/producer.py
```

---

## 2️⃣ Start Spark Streaming Consumer

```bash
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,org.postgresql:postgresql:42.7.3 \
consumer/spark_streaming.py
```

---

## 3️⃣ Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🧠 AI Fraud Detection

Transactions exceeding configured thresholds are automatically flagged as suspicious.

Example:
- High-value transactions
- Abnormal spikes
- Suspicious transaction patterns

---

# 📈 Resume Impact

This project demonstrates:

- Distributed systems knowledge
- Real-time data engineering
- Event-driven architecture
- Streaming analytics
- Production-grade pipeline design
- Dashboard engineering
- Docker infrastructure management

---

# 🔥 Future Enhancements

- 🌍 Real-time global transaction map
- 🤖 AI anomaly detection engine
- 📡 Kafka lag monitoring
- ☸ Kubernetes deployment
- 📊 Grafana integration
- ⚡ Redis caching layer
- ☁ AWS / Azure deployment
- 🧠 Machine learning prediction engine

---

# 👨‍💻 Author

### Sudhanshu Dhande

Built with ⚡ Kafka + PySpark + PostgreSQL + Streamlit

---