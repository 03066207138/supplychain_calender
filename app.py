st.set_page_config(page_title=config.PAGE_TITLE, layout="wide")

import streamlit as st
from components.calendar_view import show_calendar
from components.data_display import show_selected_data
from utils.file_loader import load_files
from utils.preprocess import preprocess_data
import config
from datetime import date

# Configure page
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide")
st.title(config.HEADER_TITLE)
st.markdown("<hr>", unsafe_allow_html=True)

# Load uploaded or sample JSON files
schedule_data, vrp_data = load_files()

# Stop if data not yet loaded
if not st.session_state.get("data_loaded", False):
    st.info("📁 Please upload both JSON files or load sample data to continue.")
    st.stop()

# Preprocess into usable dataframes and calendar-compatible events
schedule_df, deliveries_df, calendar_events = preprocess_data(schedule_data, vrp_data)

# Initialize today's data on first load
if "selected_date" not in st.session_state:
    st.session_state.selected_date = date.today()
    st.session_state.show_data = True

# Show calendar and capture click (including "Today" button)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 📆 Monthly Calendar Overview")
calendar_value = show_calendar(calendar_events)

# If calendar date is clicked, store and trigger detail display
if calendar_value and "dateClick" in calendar_value:
    st.session_state.selected_date = calendar_value["dateClick"]["date"]
    st.session_state.show_data = True

# Show detail for the selected date
show_selected_data(schedule_df, deliveries_df)

import streamlit as st
from components.calendar_view import show_calendar
from components.data_display import show_selected_data
from utils.file_loader import load_files
from utils.preprocess import preprocess_data
import config
from datetime import date

# Configure page
st.set_page_config(page_title=config.PAGE_TITLE, layout="wide")
st.title(config.HEADER_TITLE)
st.markdown("<hr>", unsafe_allow_html=True)

# Load uploaded or sample JSON files
schedule_data, vrp_data = load_files()

# Stop if data not yet loaded
if not st.session_state.get("data_loaded", False):
    st.info("📁 Please upload both JSON files or load sample data to continue.")
    st.stop()

# Preprocess into usable dataframes and calendar-compatible events
schedule_df, deliveries_df, calendar_events = preprocess_data(schedule_data, vrp_data)

# Initialize today's data on first load
if "selected_date" not in st.session_state:
    st.session_state.selected_date = date.today()
    st.session_state.show_data = True

# Show calendar and capture click (including "Today" button)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 📆 Monthly Calendar Overview")
calendar_value = show_calendar(calendar_events)

# If calendar date is clicked, store and trigger detail display
if calendar_value and "dateClick" in calendar_value:
    st.session_state.selected_date = calendar_value["dateClick"]["date"]
    st.session_state.show_data = True

# Show detail for the selected date
show_selected_data(schedule_df, deliveries_df)
