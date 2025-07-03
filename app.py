
import streamlit as st

st.set_page_config(page_title="HEC PathWise", layout="centered")
st.title("🎓 HEC PathWise: Transfer Evaluation Platform")

uploaded_files = st.file_uploader("📄 Upload one or more transcripts (PDF)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} transcript(s) uploaded successfully!")
    for file in uploaded_files:
        st.markdown(f"📂 Processing: `{file.name}`")
        st.markdown("🔍 *Parsing transcript and evaluating SAP, GPA, credit match...*")
        st.markdown("✅ *Top 5 degree program matches, ROI, and appeal options coming soon...*")

st.markdown("---")
st.markdown("Made with ❤️ by Annette Linders & HEC Partners • Powered by Echo")
