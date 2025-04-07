SHL-RAG-Assignment
SHL Assessment Intelligence Scraper 🔍
This project is a smart web scraping and analysis pipeline designed to extract and structure data from SHL’s public assessment catalog. It aims to assist HR professionals, researchers, and AI developers in accessing detailed assessment information to enable more effective candidate evaluation and job screening.

🔧 Project Overview
SHL provides a comprehensive catalog of psychometric and job-related assessments via their product catalog. However, this data isn’t readily available in a structured format. This tool addresses that gap by:

Crawling all pages of the catalog with pagination support

Visiting each individual assessment page

Extracting key details, including:

Assessment name

Description

Estimated completion time

Remote testing availability

Adaptive testing support

Direct URL

Additionally, it leverages Cohere to generate semantic embeddings from descriptions and uses FAISS to enable efficient similarity searches.

🧠 Use Cases
This scraper serves as a foundational data layer for GenAI applications such as:

Smarter job-candidate matching

Tailored assessment recommendations

Interactive HR analytics dashboards

Natural language-based assessment similarity search

🚀 Deployment
Deployed at: (deployment link or details to be added)

🛠️ Tech Stack
Selenium – For automated web crawling

BeautifulSoup – For HTML parsing

Cohere API – To generate text embeddings

FAISS – For fast vector-based similarity search

JSON – For clean, structured data output

📬 Contact
Interested in collaborating or learning more?
Feel free to connect on LinkedIn or open an issue in the repository.
