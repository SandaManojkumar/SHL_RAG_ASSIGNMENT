import streamlit as st
import requests

st.markdown("""
    <style>
        body {
            background-color: #E3F2FD;
            color: #1c1c1c;
            font-family: 'Arial', sans-serif;
        }

        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1A237E;
            text-align: center;
            margin-bottom: 30px;
        }

        .button {
            background-color: #1565C0;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 1.1rem;
            transition: background-color 0.3s ease;
            text-decoration: none;
        }

        .button:hover {
            background-color: #0D47A1;
        }

        .button-update {
            background-color: #2E7D32;
        }

        .button-update:hover {
            background-color: #1B5E20;
        }

        .card {
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            padding: 20px;
            border-left: 6px solid #1565C0;
            transition: transform 0.3s ease-in-out;
        }

        .card:hover {
            transform: scale(1.03);
        }

        .card-header {
            font-size: 1.5rem;
            font-weight: bold;
            color: #0D47A1;
        }

        .card-body {
            margin-top: 10px;
            color: #333;
        }

        .card-footer {
            text-align: right;
            margin-top: 15px;
        }

        .spinner {
            font-size: 1.5rem;
            color: #1565C0;
        }

        .warning-text {
            color: #C62828;
            font-weight: bold;
        }

        .success-text {
            color: #2E7D32;
        }

        .highlight {
            color: #EF6C00;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">SHL Assessment Recommender</div>', unsafe_allow_html=True)

FASTAPI_URL = "https://shl-rag-assignment-nt82.onrender.com"

if st.button("🔄 Update Assessment Data", key="update", help="Click to refresh the data from the backend", use_container_width=True):
    with st.spinner("Updating data..."):
        try:
            response = requests.post(f"{FASTAPI_URL}/update-data")
            if response.status_code == 200:
                st.success("✅ Data updated successfully!", icon="✅")
            else:
                st.error(f"❌ Failed to update: {response.status_code}", icon="⚠️")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}", icon="⚠️")

query = st.text_input("Enter job role or keywords:", help="Enter job role or keywords to search for relevant assessments")

if st.button("Search", key="search", help="Search assessments based on your query", use_container_width=True):
    with st.spinner("Fetching recommendations..."):
        try:
            response = requests.post(f"{FASTAPI_URL}/recommend", json={"query": query})
            if response.status_code == 200:
                results = response.json().get("results", [])
                if results:
                    st.success("Results loaded!", icon="✅")
                    for result in results:
                        with st.container():
                            st.markdown(f"""
                                <div class="card">
                                    <div class="card-header">{result.get('name', 'Untitled')}</div>
                                    <div class="card-body">
                                        <p>{result.get("description", "No description available.")}</p>
                                        <p><strong>Duration:</strong> {result.get('duration')} minutes</p>
                                        <p><strong>Remote Support:</strong> {result.get('remote_support')}</p>
                                        <p><strong>Adaptive:</strong> {result.get('adaptive')}</p>
                                    </div>
                                    <div class="card-footer">
                                        <a href="{result.get('url')}" target="_blank" class="button">More Info</a>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                else:
                    st.warning("No results found.", icon="⚠️")
            else:
                st.error("Something went wrong fetching data.", icon="⚠️")
        except Exception as e:
            st.error(f"Error fetching recommendations: {str(e)}", icon="⚠️")
