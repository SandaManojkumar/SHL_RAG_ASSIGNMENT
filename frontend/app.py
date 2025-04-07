import streamlit as st
import requests

st.markdown("""
    <style>
        body {
            background-color: #F3F0FF;
            color: #2C2C54;
            font-family: 'Segoe UI', sans-serif;
        }

        .title {
            font-size: 2.8rem;
            font-weight: 600;
            color: #5A4BFF;
            text-align: center;
            margin-bottom: 40px;
        }

        .button {
            background: rgba(255, 255, 255, 0.7);
            border: 2px solid #5A4BFF;
            color: #5A4BFF;
            padding: 12px 26px;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 500;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
        }

        .button:hover {
            background: #5A4BFF;
            color: white;
        }

        .button-update {
            background: #00C9A7;
            color: white;
            border: none;
        }

        .button-update:hover {
            background: #00B896;
        }

        .card {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            margin-bottom: 25px;
            padding: 24px;
            border-left: 6px solid #6C63FF;
            transition: transform 0.3s ease-in-out;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card-header {
            font-size: 1.5rem;
            font-weight: 600;
            color: #403B91;
        }

        .card-body {
            margin-top: 12px;
            color: #4D4D66;
            line-height: 1.6;
        }

        .card-footer {
            text-align: right;
            margin-top: 20px;
        }

        .spinner {
            font-size: 1.5rem;
            color: #6C63FF;
        }

        .warning-text {
            color: #FF6B6B;
            font-weight: bold;
        }

        .success-text {
            color: #00C9A7;
        }

        .highlight {
            color: #FFA726;
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
