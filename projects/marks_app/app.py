from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("add.html")  

@app.route("/submit_marks", methods=["POST"])
def submit_marks():
    student_name = request.form['student_name']
    subject = request.form['subject']
    marks = request.form['marks']
    return f"Received: {student_name} - {subject} - {marks}"

if __name__ == "__main__":
    app.run(debug=True)
