import streamlit as st
import requests

theme = st.selectbox("Choose Theme:", ["Dark Mode", "Light Mode"])

if theme == "Dark Mode":
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: #f0f0f0;
                font-family: 'Segoe UI', sans-serif;
            }
            .title { color: #00e6e6; }
            .card { background-color: rgba(255, 255, 255, 0.05); color: #eee; border-left: 6px solid #00e6e6; }
            .card-header { color: #00e6e6; }
            .button {
                background: linear-gradient(to right, #00c6ff, #0072ff);
                color: white;
            }
            .button:hover {
                background: linear-gradient(to right, #0072ff, #00c6ff);
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #f8f9fa, #e9ecef);
                color: #333;
                font-family: 'Segoe UI', sans-serif;
            }
            .title { color: #1a237e; }
            .card { background-color: white; color: #333; border-left: 6px solid #1a73e8; }
            .card-header { color: #1a237e; }
            .button {
                background: linear-gradient(to right, #1a73e8, #1976d2);
                color: white;
            }
            .button:hover {
                background: linear-gradient(to right, #1976d2, #1a73e8);
            }
        </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title" style="text-align:center; font-size:2.5rem; font-weight:bold;">SHL Assessment Recommender</div>', unsafe_allow_html=True)

FASTAPI_URL = "https://shl-rag-assignment-nt82.onrender.com"

if st.button("🔄 Update Assessment Data", key="update", use_container_width=True):
    with st.spinner("Updating data..."):
        try:
            response = requests.post(f"{FASTAPI_URL}/update-data")
            if response.status_code == 200:
                st.success("✅ Data updated successfully!", icon="✅")
            else:
                st.error(f"❌ Failed to update: {response.status_code}", icon="⚠️")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}", icon="⚠️")

query = st.text_input("Enter job role or keywords:")

if st.button("Search", key="search", use_container_width=True):
    with st.spinner("Fetching recommendations..."):
        try:
            response = requests.post(f"{FASTAPI_URL}/recommend", json={"query": query})
            if response.status_code == 200:
                results = response.json().get("results", [])
                if results:
                    st.success("Results loaded!", icon="✅")
                    for result in results:
                        st.markdown(f"""
                            <div class="card" style="border-radius: 12px; padding: 20px; margin: 15px 0; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
                                <div class="card-header" style="font-size: 1.3rem; font-weight: bold;">{result.get('name', 'Untitled')}</div>
                                <div class="card-body" style="margin-top: 10px;">
                                    <p>{result.get("description", "No description available.")}</p>
                                    <p><strong>Duration:</strong> {result.get('duration')} minutes</p>
                                    <p><strong>Remote Support:</strong> {result.get('remote_support')}</p>
                                    <p><strong>Adaptive:</strong> {result.get('adaptive')}</p>
                                </div>
                                <div class="card-footer" style="text-align:right; margin-top:10px;">
                                    <a href="{result.get('url')}" target="_blank" class="button" style="padding:10px 20px; border-radius: 8px; text-decoration:none;">More Info</a>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("No results found.", icon="⚠️")
            else:
                st.error("Something went wrong fetching data.", icon="⚠️")
        except Exception as e:
            st.error(f"Error fetching recommendations: {str(e)}", icon="⚠️")
