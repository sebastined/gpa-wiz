from flask import Flask, request, jsonify, send_from_directory
import os
from fpdf import FPDF  # For generating the downloadable PDF

app = Flask(__name__, static_folder="static")

GRADE_POINTS = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/calc_gpa", methods=["POST"])
def calc_gpa():
    try:
        data = request.get_json(force=True)
        courses = data.get("courses", [])
        if not courses:
            return jsonify({"error": "No courses provided"}), 400

        total_points = 0
        total_credits = 0

        for c in courses:
            grade = c.get("grade", "").upper()
            credit = float(c.get("credit", 0))
            if grade not in GRADE_POINTS:
                return jsonify({"error": f"Invalid grade '{grade}'"}), 400
            total_points += GRADE_POINTS[grade] * credit
            total_credits += credit

        if total_credits == 0:
            return jsonify({"error": "Total credits cannot be zero"}), 400

        gpa = round(total_points / total_credits, 2)
        return jsonify({"gpa": gpa, "scale": "5.0"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/download_report", methods=["POST"])
def download_report():
    """Generate a simple GPA report PDF."""
    data = request.get_json(force=True)
    gpa = data.get("gpa")
    courses = data.get("courses", [])

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "GPA-WIZ Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"GPA: {gpa} / 5.0", ln=True)

    pdf.ln(5)
    pdf.cell(0, 10, "Course Details:", ln=True)

    pdf.set_font("Arial", "", 11)
    for c in courses:
        pdf.cell(0, 8,
            f"{c.get('code')} - {c.get('credit')} credits - Grade: {c.get('grade')}",
            ln=True)

    os.makedirs("reports", exist_ok=True)
    filepath = os.path.join("reports", "gpa_report.pdf")
    pdf.output(filepath)

    return jsonify({"file": "gpa_report.pdf"})


@app.route("/reports/<path:filename>")
def serve_report(filename):
    return send_from_directory("reports", filename)


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    print("🎓 GPA-WIZ running at: http://127.0.0.1:8080")
    app.run(host="0.0.0.0", port=8080)
