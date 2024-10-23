from flask import Flask, jsonify

app = Flask(__name__)


students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
    {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
    {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
    {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
    {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
    {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
]

@app.route("/old_students/", methods=['GET'])
def get_old_students():
    old_students = []
    for student_obj in students:
        if student_obj['age'] > 20:
            old_students.append(student_obj)
    return old_students

@app.route("/young_students/", methods=['GET'])
def get_young_students():
    young_students = []
    for student_obj in students:
        if student_obj['age'] < 21:
            young_students.append(student_obj)
    return young_students

@app.route("/advance_students/", methods=['GET'])
def get_advance_students():
    advance_students = []
    for student_obj in students:
        if student_obj["age"] < 21 and student_obj["grade"] == 'A':
            advance_students.append(student_obj)
    return advance_students

@app.route("/student_names/", methods=['GET'])
def get_student_names():
    student_names = []
    for student_obj in students:
        names_dict = {}
        names_dict["first_name"] = student_obj["first_name"]
        names_dict["last_name"] = student_obj["last_name"]
        student_names.append(names_dict)

    return student_names

@app.route("/student_ages/", methods=['GET'])
def get_student_ages():
    student_ages = []
    for student_obj in students:
        ages_dict = {}
        ages_dict["first_name"] = student_obj["first_name"]
        ages_dict["last_name"] = student_obj["last_name"]
        ages_dict["age"] = student_obj["age"]
        student_ages.append(ages_dict)
        
    return student_ages

@app.route("/all_students/", methods=['GET'])
def get_all_students():
    all_students = []
    for student_obj in students:
        all_students.append(student_obj)
    return all_students


@app.route("/", methods=['GET'])
def home():
    return "<h1>Yankee Student Portal</h1>"

app.run(debug=True, port=8000)