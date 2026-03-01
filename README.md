# 📊 Project: Relational Affinity & Transactional Topology

## 📝 Overview

This project involves a **Forensic Data Engineering** workflow designed to map relationships across a network of 100 distinct entities. By transforming raw, unstructured transaction logs and fragmented member metadata into a **Weighted Adjacency Matrix**, the system reveals patterns of interaction, frequency, and financial magnitude.

## 🛠️ The Technical Process (ETL Pattern)

The solution follows a strict **Extract, Transform, Load (ETL)** pattern using foundational Python logic:

1. **Extraction**: Aggregates data from 100 individual member profile files and a central transaction ledger.
2. **Transformation (Entity Resolution)**: Maps anonymous system IDs to a master identity list, ensuring all 100 nodes are represented regardless of activity level.
3. **Normalization**: Calculates the **mean transaction value** between every possible sender-receiver pair. This prevents single "outlier" transactions from distorting the perceived strength of a relationship.
4. **Loading**: Outputs a tab-separated matrix (`the_matrix.txt`) sorted alphabetically to ensure consistent data indexing for downstream BI tools.

## 💼 Business Use Case: Systemic Risk Mapping

While framed as a criminal investigation, this process represents a **Universal Design Pattern** for:

* **Supply Chain Resilience**: Identifying "Single Points of Failure" by mapping the average dependency between 100 global suppliers.
* **Infrastructure Monitoring**: Visualizing latency and data flow between 100 microservices in a cloud ecosystem.
* **Customer Relationship Intelligence**: Quantifying the "Affinity Score" between users and product categories to drive recommendation engines.

## 📊 Key Deliverables

* **`transactions.txt`**: The raw event stream (Source Data).
* **`the_matrix.txt`**: The processed Adjacency Matrix (Information Layer).
* **`Book.xlsx`**: The final Business Intelligence report (Actionable Insight).
