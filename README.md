# SHL-RAG-assignment
# SHL Assessment Intelligence Scraper 🔍

This project provides a smart web scraping and analysis pipeline to extract and analyze SHL's public assessment catalog. It is built to help HR teams, researchers, or AI developers gain structured access to detailed assessment data for smarter job screening and candidate evaluation.

## 🔧 Project Overview

SHL offers a wide range of psychometric and job-related assessments through their [product catalog](https://www.shl.com/solutions/products/product-catalog/). However, this data is not directly available in structured format. This tool:

- Crawls all product pages with pagination.
- Visits each individual assessment page.
- Extracts key information such as:
  - Assessment name
  - Description
  - Approximate completion time
  - Remote testing availability
  - Adaptive testing support
  - Direct URL
- Uses [Cohere](https://cohere.com/) to generate semantic embeddings of descriptions.
- Indexes the data using [FAISS](https://github.com/facebookresearch/faiss) for fast similarity search.

---

## 🧠 Use Case

This scraper serves as the data backbone for Gen AI applications such as:

- Enhanced job-candidate matching
- Personalized assessment recommendations
- HR analytics dashboards
- Assessment similarity search using natural language

---
## Deployed at:
https://sandamanojkumarshlrag.streamlit.app/

---
## Tech Stack

Selenium – Automated web scraping
BeautifulSoup – HTML parsing
Cohere API – Language embedding
FAISS – Efficient vector similarity search
JSON – Structured output

---

## 📬 Contact
Feel free to reach out via LinkedIn or open an issue if you'd like to collaborate!
https://www.linkedin.com/in/manojkumar-sanda-767025213/
