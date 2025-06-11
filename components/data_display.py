import streamlit as st

def show_selected_data(schedule_df, deliveries_df):
    with st.form("date_form"):
        st.markdown("### 🔍 Select a Date to View Details")
        selected_date = st.date_input("Choose Date")
        submit_btn = st.form_submit_button("🎯 Show Data")

    if submit_btn:
        selected_str = selected_date.strftime("%Y-%m-%d")
        st.markdown(f"### 📋 Data for `{selected_str}`")

        schedule_day = schedule_df[schedule_df["date"] == selected_str]
        delivery_day = deliveries_df[deliveries_df["date"] == selected_str]

        st.markdown("#### 🌱 Scheduled Plantings")
        if not schedule_day.empty:
            for _, row in schedule_day.iterrows():
                st.markdown(f"""
                <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 10px; margin-bottom: 10px; background-color: #f1f8e9;'>
                    <b>🧭 Polygon:</b> {row['polygon']}<br>
                    <b>🌿 Specie:</b> <span style='color:#2e7d32;'>{row['specie']}</span><br>
                    <b>🏭 Supplier:</b> <span style='color:#0277bd;'>{row['supplier']}</span><br>
                    <b>📦 Amount:</b> {row['amount']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No scheduled plantings.")

        st.markdown("#### 🚚 Deliveries")
        if not delivery_day.empty:
            for _, row in delivery_day.iterrows():
                st.markdown(f"""
                <div style='border: 1px solid #e0e0e0; border-radius: 10px; padding: 10px; margin-bottom: 10px; background-color: #e3f2fd;'>
                    <b>📍 Polygon:</b> {row['polygon']}<br>
                    <b>📦 Amount Delivered:</b> {row['amount']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No deliveries recorded.")
