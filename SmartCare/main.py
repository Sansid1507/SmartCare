
from flask import Flask, render_template
from agents.health_monitor_agent import get_health_status
from agents.reminder_agent import get_reminders
from services.database_service import save_data

app = Flask(__name__, template_folder="interfaces/dashboard_ui", static_folder="interfaces/dashboard_ui")

@app.route("/")
def dashboard():
    health = get_health_status()
    reminders = get_reminders()
    save_data(health)
    return render_template("index.html", health=health, reminders=reminders)

if __name__ == "__main__":
    app.run(debug=True)
