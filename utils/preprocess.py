import pandas as pd
from datetime import datetime

def preprocess_data(schedule_data, vrp_data):
    schedule_df = pd.DataFrame(schedule_data)
    schedule_df["date"] = schedule_df["day"].apply(lambda d: datetime(2025, 6, d).strftime("%Y-%m-%d"))

    delivery_rows = []
    for record in vrp_data:
        day = record["day"]
        date_str = datetime(2025, 6, day).strftime("%Y-%m-%d")
        for action in record["actions"]:
            if action[0] == "deliver":
                delivery_rows.append({
                    "day": day,
                    "date": date_str,
                    "polygon": action[1]["polygon"],
                    "amount": action[1]["amount"]
                })
    deliveries_df = pd.DataFrame(delivery_rows)

    calendar_events = []
    for _, row in deliveries_df.iterrows():
        calendar_events.append({
            "title": f"📦 P{row['polygon']} - {row['amount']}",
            "start": row["date"],
            "end": row["date"],
            "color": "#0d6efd"
        })

    for _, row in schedule_df.iterrows():
        short_specie = row['specie'].split()[0] if row['specie'] else "Specie"
        calendar_events.append({
            "title": f"🌿 P{row['polygon']} - {row['amount']} {short_specie}",
            "start": row["date"],
            "end": row["date"],
            "color": "#198754"
        })

    return schedule_df, deliveries_df, calendar_events
