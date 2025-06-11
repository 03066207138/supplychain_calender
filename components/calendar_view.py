from datetime import datetime
from streamlit_calendar import calendar

def show_calendar(events):
    today_str = datetime.today().strftime('%Y-%m-%d')

    config = {
        "initialView": "timeGridWeek",
        "initialDate": today_str,
        "themeSystem": "bootstrap5",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridDay,timeGridWeek,listWeek"
        },
        "height": 700,
        "editable": False,
        "selectable": True,
        "nowIndicator": True,
        "slotMinTime": "06:00:00",
        "slotMaxTime": "20:00:00",
        "scrollTime": "08:00:00",
        "dateClick": True
    }

    custom_css = {
        "body": {"backgroundColor": "#f8f9fa", "color": "#212529"},
        ".fc": {"backgroundColor": "#ffffff", "color": "#212529"},
        ".fc-toolbar-title": {"color": "#212529", "fontWeight": "600"},
        
        ".fc-button": {
        "backgroundColor": "#dc3545",       # Red buttons (default)
        "border": "none",
        "color": "white",
        "fontWeight": "500"
        },
        
        ".fc-button:hover": {
        "backgroundColor": "#ffffff",       # 🔁 Hover background white
        "color": "#000000",                 # 🔁 Hover text black
        "border": "1px solid #dc3545"
         },
        
        ".fc-button-active": {
        "backgroundColor": "#212529",       # Active button (e.g., "day") color
        "color": "white",
        "fontWeight": "600"
        }, 
        
         ".fc-button-active:hover": {
         "backgroundColor": "#ffffff",       # Optional: white hover for active
         "color": "#000000"
        },

        ".fc-button:hover": {
        "backgroundColor": "#b02a37"  # Darker red hover
        
        },
        
        ".fc-daygrid-day-number": {"color": "#495057"},
        ".fc-timegrid-slot-label": {"color": "#495057"},
        ".fc-col-header-cell-cushion": {"color": "#343a40", "fontWeight": "600"},
        ".fc-scrollgrid": {"borderColor": "#dee2e6"},
        ".fc-event": {
            "border": "none",
            "fontWeight": "500",
            "color": "black"
        },
        ".fc-daygrid-day": {"backgroundColor": "#ffffff"},
        ".fc-timegrid-slot": {"backgroundColor": "#f1f3f5"},
        ".fc-now-indicator-line": {"borderColor": "#dc3545"}
    }

    return calendar(events=events, options=config, custom_css=custom_css)
