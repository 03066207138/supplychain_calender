import streamlit as st
import json
from config import SAMPLE_SCHEDULE, SAMPLE_VRP

def load_files():
    st.sidebar.header("📂 Upload JSON Files")
    schedule_file = st.sidebar.file_uploader("📄 supply_chain_schedule.json", type="json")
    vrp_file = st.sidebar.file_uploader("📄 vrp_actions.json", type="json")

    # Init session keys
    if "data_loaded" not in st.session_state:
        st.session_state.data_loaded = False
        st.session_state.schedule_data = None
        st.session_state.vrp_data = None

    if st.sidebar.button("📊 Load Uploaded Data"):
        if schedule_file and vrp_file:
            st.session_state.schedule_data = json.load(schedule_file)
            st.session_state.vrp_data = json.load(vrp_file)
            st.session_state.data_loaded = True
            st.success("✅ Files loaded successfully.")
        else:
            st.warning("⚠️ Please upload both files.")

    if st.sidebar.checkbox("🔍 Use Sample Data Instead"):
        with open(SAMPLE_SCHEDULE) as f:
            st.session_state.schedule_data = json.load(f)
        with open(SAMPLE_VRP) as f:
            st.session_state.vrp_data = json.load(f)
        st.session_state.data_loaded = True
        st.success("✅ Sample data loaded.")

    # Return from session
    return st.session_state.schedule_data, st.session_state.vrp_data
