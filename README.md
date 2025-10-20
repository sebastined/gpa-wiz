
# GPA-WIZ 🎓

**GPA-WIZ** is a simple and interactive web application that allows students to calculate their GPA/CGPA on a 5.0 scale. Users can input course codes, credits, and grades, and instantly calculate their GPA. The app also supports **dynamic course addition**, **dark/light mode**, and **PDF report download**.

---

## Features

* Enter multiple courses with **course codes, credits, and grades**.
* Calculate GPA on a **5.0 scale**.
* Add or remove courses dynamically.
* Toggle between **light and dark mode**.
* Download a **PDF report** of your GPA.
* Responsive and user-friendly UI.
* Footer with dynamic year and credit information.

---

## Grade to Point Conversion

| Grade | Point |
| ----- | ----- |
| A     | 5     |
| B     | 4     |
| C     | 3     |
| D     | 2     |
| F     | 1     |

---

## Demo

![GPA-WIZ Screenshot](link-to-screenshot-if-any)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/sebastined/gpa-wiz.git
cd gpa-wiz
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> If you don’t have `requirements.txt`, you can install manually:

```bash
pip install flask fpdf
```

---

## Running the App

```bash
python app.py
```

Open your browser and visit: [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

## Usage

1. Enter **course code**, **credits**, and **grade** for each course.
2. Click **“+ Add Course”** to add more courses.
3. Click **“Calculate GPA”** to get your GPA.
4. Click **“Download Report”** to save a PDF of your results.
5. Toggle **dark/light mode** using the button on the top-right.

---

## Project Structure

```
gpa-wiz/
│
├─ app.py                 # Flask backend
├─ requirements.txt       # Python dependencies
├─ reports/               # Generated PDF reports
├─ static/
│  └─ index.html          # Frontend HTML/CSS/JS
└─ README.md
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is open-source and available under the **MIT License**.

---

## Author

**Sebastine Nnanemere** & ChatGPT


