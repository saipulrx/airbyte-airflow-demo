# Hands-on Airbyte, Apache Airflow, PostgreSQL and BigQuery 
This repository for course Data Product II in Partnatech. 
In this course use tech stack : 
- Data Ingestion : Airbyte
- Workflow Orchestions : Apache Airflow
- Data Platform : OLTP(PostgreSQL) & OLAP(BigQuery)

## Prerequisite
1) Already installed docker and docker compose
2) Already have service account key json file for Google BigQuery
3) Already installed postgresql in local
4) Already installed vscode or other IDE

## Table of Content
1) Setup Airbyte in docker
2) Define source connection in Airbyte
3) Define destination connection in Airbyte
4) Configure connection
5) EL Data Architecture
6) Create airflow dags for trigger Airbyte job

### Setup Airbyte in docker
- git clone this code to local
- run docker compose
  ```
  docker compose up -d
  ``` 
- If success then open url http://localhost:8000 for Airbyte UI

