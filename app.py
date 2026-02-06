from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    project_list = [
        {
            "name": "Portfolio Website",
            "description": "Personal portfolio built with Flask and Tailwind CSS.",
            "github": "https://github.com/yourusername/portfolio"
        },
        {
            "name": "Lungcare+",
            "description": "This project is designed to provide preliminary screening and guided consultation for lung-related diseases. By leveraging a custom CNN model, the system analyzes lung scans to detect possible cancer. Through a simple chatbot interface, it guides users to relevant doctors or symptom-based resources, offering a user-friendly, accessible, and supportive diagnostic aid.",
            "github": "https://github.com/divyanshi2203/Lungcare-.git"
        },

        {
            "name": "The-Data-Morph-JSON-to-Insights",
            "description": "A dynamic data platform that automates the retrieval, transformation, and visualization of real-time city-based weather and news data.",
            "github": "https://github.com/divyanshi2203/-The-Data-Morph-JSON-to-Insights.git"
        }
    ]
    return render_template("projects.html", projects=project_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        with open("contacts.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), name, email, message])

        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
