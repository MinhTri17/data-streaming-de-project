# Project Title
### | **Real-time Data streaming**

# Overview
This project builds a data streaming pipeline using Apache Airflow to orchestrate data ingestion from an external API source, processing and streaming to Apache Kafka. The Kafka stream is consumed and processed using Apache Spark (with master-worker nodes setup). Finally, data is loaded into Apache Cassandra for storage and analytics. All components are containerized using Docker 

**📌 Note:** This project was developed for learning purpose by following a tutorial, with the goal of understanding how to design and implement a data streaming pipeline using modern data engineering technologies

# Objectives
- Understand setting up Apache Airflow tasks
- Learn how to stream data using Apache Kafka and how it works with Apache Airflow and Apache Spark
- Utilize Apache Spark for streamed data processing
- Store streamed data in Cassandra
- Apply Docker for setting up configuration for all components
  
# Project Architecture


- **Apache Airflow, PostgreSQL**: orchestrates the pipeline and manages Airflow's metadata
- **Apache Kafka, Zookeeper:** streams data in real-time between components
- **Control Center:** monitors Kafka activity
- **Schema Registry:** manages schema of the Kafka message
- **Apache Spark:** consumes Kafka stream data, processes it and writes the results to Cassandra
- **Cassandra:** acts as the database for storing the final processed streaming data
- **Docker:** containerizes each components and manages their local setup
  
# Tech Stack
- **Workflow & Orchestration:** Apache Airflow, PostgreSQL
- **Streaming:** Apache Kafka
- **Data Processing:** Apache Spark
- **Data Storage:** Cassandra
- **Language:** Python
  
# Reference Tutorial
- This project is based on the following tutorial: [Realtime Data Streaming | End To End Data Engineering Project](https://www.youtube.com/watch?v=GqAcTrqKcrY)
- The implementation and explanation in this repository reflect my own learning
