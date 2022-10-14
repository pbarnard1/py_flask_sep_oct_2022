from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
from flask_app.models import student

class Teacher:
    db_name = "students_teachers_schema" # CHANGE THIS TO MATCH YOUR SCHEMA NAME!  Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.subject = data["subject"]
        self.is_tenured = data["is_tenured"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.students = [] # Hold a bunch of Students
        self.semester = None # Hold the semester when we are linking to a student
        # Uses a ternary operator: value_if_true if condition_is_true else value_if_false
        self.num_students = data["num_students"] if "num_students" in data else 0
        # We might need other attributes to hold additional values from your queries
    
    @classmethod
    def add_teacher(cls, data):
        query = """
        INSERT INTO teachers
        (first_name, last_name, is_tenured, subject, email)
        VALUES
        (%(first_name)s, %(last_name)s, %(is_tenured)s, %(subject)s, %(email)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_teachers(cls):
        # CORRECTED: changed from SELECT *, COUNT(student_id) to
        # "SELECT teachers.*, COUNT(student_id)" due to it not working for some folks
        query = """
        SELECT teachers.*, COUNT(student_id) AS num_students FROM teachers
        LEFT JOIN students_teachers
        ON teachers.id = students_teachers.teacher_id
        GROUP BY teachers.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        if len(results) == 0:
            return []
        else:
            all_teachers = []
            for cur_teacher_dictionary in results:
                # Create the Student
                cur_teacher_instance = cls(cur_teacher_dictionary)
                # Add to the list
                all_teachers.append(cur_teacher_instance)
            return all_teachers

    @classmethod
    def get_teachers_who_have_not_taught_student(cls, data):
        query = """
        SELECT * FROM teachers 
        WHERE teachers.id 
        NOT IN 
        (SELECT teacher_id FROM students_teachers WHERE student_id = %(id)s);
        """
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) == 0:
            return []
        else:
            all_teachers = []
            for cur_teacher_dictionary in results:
                # Create the Student
                cur_teacher_instance = cls(cur_teacher_dictionary)
                # Add to the list
                all_teachers.append(cur_teacher_instance)
            return all_teachers

    @classmethod
    def grab_one_teacher_with_students(cls, data):
        query = """
        SELECT * FROM teachers 
        LEFT JOIN students_teachers
        ON teachers.id = students_teachers.teacher_id
        LEFT JOIN students
        ON students.id = students_teachers.student_id
        WHERE teachers.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        else:
            # Create the Teacher class instance
            this_teacher_instance = cls(results[0])
            if results[0]["students.id"] != None: # At least one student is found
                # Loop through each student dictionary
                for current_student_dictionary in results:
                    # Create the Student class instance
                    student_instance = student.Student({
                        "id": current_student_dictionary["students.id"],
                        "first_name": current_student_dictionary["students.first_name"],
                        "last_name": current_student_dictionary["students.last_name"],
                        "email": current_student_dictionary["students.email"],
                        "birthdate": current_student_dictionary["birthdate"],
                        "created_at": current_student_dictionary["students.created_at"],
                        "updated_at": current_student_dictionary["students.updated_at"],
                    })
                    student_instance.semester = current_student_dictionary["semester"] # Tie the semester in
                    this_teacher_instance.students.append(student_instance)
            return this_teacher_instance

    @classmethod
    def remove_teacher(cls, data):
        query = """
        DELETE FROM teachers WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)