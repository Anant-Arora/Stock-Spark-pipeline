#  Real-Time Stock Market Insights Pipeline (Simulated HFT)

A scalable real-time data engineering pipeline that ingests stock market data using Kafka, processes it with Apache Spark, and persists it to a SQL Server database — all deployed on Google Cloud Platform (GCP). Designed to simulate the data flow and insights of high-frequency trading (HFT) systems.

---

##  About the Project

This project demonstrates how to build a robust real-time streaming pipeline for stock market data. It fetches live data using the Yahoo Finance API, streams it via Apache Kafka, processes and transforms the data using Spark Structured Streaming, and writes it to a SQL Server database for analytics and visualization.

The entire setup is built from scratch using virtual machines and Dataproc clusters on GCP..

---

## 🛠️ Tech Stack

- **Data Ingestion**: Yahoo Finance API
- **Streaming Platform**: Apache Kafka (with Zookeeper)
- **Data Processing**: Apache Spark Structured Streaming
- **Data Storage**: Microsoft SQL Server (remote)
- **Cloud Infrastructure**: Google Cloud Platform (GCP)
  - Compute Engine VMs
  - Dataproc (for running Spark jobs)
  - Cloud NAT (for internet access on internal nodes)
  - Cloud Storage (for file and notebook handling)
- **Languages**: Python (Kafka Producer & Spark Consumer)

---

##  Architecture

![Architecture](path/to/your/architecture/image.png)

---

##  Use Cases

- Simulate a **High-Frequency Trading (HFT)** data pipeline.
- Build real-time **dashboards or alerts** based on market movements.
- Serve as a **template** for real-time analytics pipelines in fintech or IoT.
- Educational tool for learning real-time data engineering on cloud infrastructure.

---

##  What Could Be Better

Due to GCP's **free-tier limitations**, the following constraints were intentionally applied:

- A **single-node Dataproc cluster** was used to reduce costs.
- The **producer script includes sleep intervals** to reduce load and API calls.
- **Only internal IPs** were used initially, requiring extra NAT and networking configuration for internet access.
- **Limited data volume** was processed — for a full-scale pipeline, larger and more resilient cluster setups are recommended.

Despite these, the project remains fully functional and scalable with minor adjustments.

---

##  Known Limitations / Cons

- **Single Zookeeper & Kafka node** — No replication or fault tolerance.
- **Manual configuration** of internal/external IPs and NAT was required for component communication.
- **Producer failure tolerance** not implemented — a crash in producer halts ingestion.
- **Lack of monitoring tools** like Prometheus, Grafana, or alerting mechanisms.
- **No automated deployment** — setup and configuration is manual.

---

##  Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests for improvements or extensions — especially for:
- Adding Prometheus/Grafana monitoring
- CI/CD setup
- Dockerized or Terraform-based deployment

---


