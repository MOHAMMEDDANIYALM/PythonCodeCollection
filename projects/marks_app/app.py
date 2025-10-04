from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database/students.db'

# ----------------------
# Database connection
# ----------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ----------------------
# Home Page
# ----------------------
@app.route('/')
def index():
    return render_template('index.html')

# ----------------------
# Add Student
# ----------------------
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        uucms = request.form['uucms']
        name = request.form['name']
        age = request.form['age']

        conn = get_db_connection()
        conn.execute('INSERT INTO students (uucms, name, age) VALUES (?, ?, ?)',
                     (uucms, name, age))
        conn.commit()
        conn.close()
        return redirect(url_for('students'))
    return render_template('add.html')

# ----------------------
# Edit Student
# ----------------------
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    if student is None:
        conn.close()
        return "Student not found!"

    if request.method == 'POST':
        uucms = request.form['uucms']
        name = request.form['name']
        age = request.form['age']

        conn.execute('UPDATE students SET uucms=?, name=?, age=? WHERE id=?',
                     (uucms, name, age, id))
        conn.commit()
        conn.close()
        return redirect(url_for('students'))

    conn.close()
    return render_template('edit_student.html', student=student)

# ----------------------
# Add/Edit Marks
# ----------------------
@app.route('/add_marks/<int:student_id>', methods=['GET', 'POST'])
def add_marks(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id=?', (student_id,)).fetchone()
    if student is None:
        conn.close()
        return "Student not found!"

    marks = conn.execute('SELECT * FROM marks WHERE student_id=?', (student_id,)).fetchone()

    if request.method == 'POST':
        msc = int(request.form['msc'])
        evs = int(request.form['evs'])
        doc = int(request.form['doc'])
        eng = int(request.form['eng'])
        hin = int(request.form['hin'])
        c = int(request.form['c'])

        total = msc + evs + doc + eng + hin + c
        cgpa = round(total / 6, 2)

        if marks:
            conn.execute('''
                UPDATE marks SET msc=?, evs=?, doc=?, eng=?, hin=?, c=?, total=?, cgpa=? 
                WHERE student_id=?
            ''', (msc, evs, doc, eng, hin, c, total, cgpa, student_id))
        else:
            conn.execute('''
                INSERT INTO marks (student_id, msc, evs, doc, eng, hin, c, total, cgpa)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, msc, evs, doc, eng, hin, c, total, cgpa))

        conn.commit()
        conn.close()
        return redirect(url_for('students'))

    conn.close()
    return render_template('add_marks.html', student=student, marks=marks)

# ----------------------
# View All Students (with search)
# ----------------------
@app.route('/students', methods=['GET'])
def students():
    search = request.args.get('search', '').strip()
    conn = get_db_connection()

    if search:
        students_list = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR uucms LIKE ?",
            (f'%{search}%', f'%{search}%')
        ).fetchall()
    else:
        students_list = conn.execute("SELECT * FROM students").fetchall()

    marks_list = conn.execute("SELECT * FROM marks").fetchall()

    # Combine data
    students_data = []
    for student in students_list:
        marks = next((m for m in marks_list if m['student_id'] == student['id']), None)
        total = marks['total'] if marks else '-'
        cgpa = marks['cgpa'] if marks else '-'

        students_data.append({
            'student': student,
            'marks': marks,
            'total': total,
            'cgpa': cgpa
        })

    conn.close()
    return render_template('students.html', students_data=students_data, search=search)

# ----------------------
# Student view their own marks
# ----------------------
@app.route('/view_marks', methods=['GET', 'POST'])
def view_marks():
    student_data = []
    if request.method == 'POST':
        query = request.form['query'].strip()
        conn = get_db_connection()

        students_list = conn.execute(
            "SELECT * FROM students WHERE uucms=? OR name LIKE ?",
            (query, f"%{query}%")
        ).fetchall()

        marks_list = conn.execute("SELECT * FROM marks").fetchall()

        for student in students_list:
            marks = next((m for m in marks_list if m['student_id'] == student['id']), None)
            total = sum([marks['msc'], marks['evs'], marks['doc'], marks['eng'], marks['hin'], marks['c']]) if marks else '-'
            cgpa = round(total / 6, 2) if marks else '-'

            student_data.append({
                'student': student,
                'marks': marks if marks else {'msc':'-', 'evs':'-', 'doc':'-', 'eng':'-', 'hin':'-', 'c':'-'},
                'total': total,
                'cgpa': cgpa
            })

        conn.close()

    return render_template('student_marks.html', student_data=student_data)

# ----------------------
# Student Marks Page (All students sorted by CGPA)
# ----------------------
@app.route('/student_marks', methods=['GET'])
def student_marks():
    search = request.args.get('search', '').strip()
    conn = get_db_connection()

    # Get all students (with optional search)
    if search:
        students_list = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR uucms LIKE ?",
            (f'%{search}%', f'%{search}%')
        ).fetchall()
    else:
        students_list = conn.execute("SELECT * FROM students").fetchall()

    # Get all marks
    marks_list = conn.execute("SELECT * FROM marks").fetchall()
    conn.close()

    # Combine student + marks data
    students_data = []
    for student in students_list:
        marks = next((m for m in marks_list if m['student_id'] == student['id']), None)
        total = marks['total'] if marks else None
        cgpa = marks['cgpa'] if marks else 0  # 0 for sorting students without marks

        students_data.append({
            'student': student,
            'marks': marks,
            'total': total if total is not None else '-',
            'cgpa': cgpa if cgpa != 0 else '-'  # display '-' if no CGPA
        })

    # Sort students by CGPA descending
    students_data.sort(key=lambda x: x['cgpa'] if isinstance(x['cgpa'], float) else -1, reverse=True)

    return render_template('student_marks.html', students_data=students_data, search=search)

# ----------------------
# Run the App
# ----------------------
if __name__ == '__main__':
    app.run(debug=True)
