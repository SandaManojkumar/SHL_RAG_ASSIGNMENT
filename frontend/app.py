import streamlit as st
import requests

st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }

        .title {
            font-size: 2.7rem;
            font-weight: bold;
            color: #00e6e6;
            text-align: center;
            margin-bottom: 30px;
        }

        .button {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            padding: 12px 24px;
            border-radius: 10px;
            font-size: 1.1rem;
            border: none;
            transition: all 0.3s ease;
            text-decoration: none;
        }

        .button:hover {
            background: linear-gradient(to right, #0072ff, #00c6ff);
            transform: scale(1.03);
        }

        .button-update {
            background: linear-gradient(to right, #00c853, #64dd17);
        }

        .button-update:hover {
            background: linear-gradient(to right, #64dd17, #00c853);
        }

        .card {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
            padding: 20px;
            border-left: 6px solid #00e6e6;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease-in-out;
        }

        .card:hover {
            transform: scale(1.02);
        }

        .card-header {
            font-size: 1.5rem;
            font-weight: bold;
            color: #00e6e6;
        }

        .card-body {
            margin-top: 10px;
            color: #ddd;
        }

        .card-footer {
            text-align: right;
            margin-top: 15px;
        }

        .spinner {
            font-size: 1.5rem;
            color: #00e6e6;
        }

        .warning-text {
            color: #ff5252;
            font-weight: bold;
        }

        .success-text {
            color: #00e676;
        }

        .highlight {
            color: #ffb300;
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
