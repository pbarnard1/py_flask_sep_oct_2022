from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
from flask_app.models import teacher

class Student:
    db_name = "students_teachers_schema" # CHANGE THIS TO MATCH YOUR SCHEMA NAME!  Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.birthdate = data["birthdate"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.teachers = [] # Hold a bunch of Teachers
        self.semester = None # Hold the semester when we are linking to a teacher
        # Uses a ternary operator: value_if_true if condition_is_true else value_if_false
        self.num_teachers = data["num_teachers"] if "num_teachers" in data else 0
        # We might need other attributes to hold additional values from your queries - or values from middle tables
    
    @classmethod
    def add_student(cls, data):
        query = """
        INSERT INTO students
        (first_name, last_name, birthdate, email)
        VALUES
        (%(first_name)s, %(last_name)s, %(birthdate)s, %(email)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_students(cls):
        # CORRECTED: changed from SELECT *, COUNT(teacher_id) to
        # "SELECT students.*, COUNT(teacher_id)" due to it not working for some folks
        query = """
        SELECT students.*, COUNT(teacher_id) AS num_teachers FROM students
        LEFT JOIN students_teachers
        ON students.id = students_teachers.student_id
        GROUP BY students.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        if len(results) == 0:
            return []
        else:
            all_students = []
            for cur_student_dictionary in results:
                # Create the Student
                cur_student_instance = cls(cur_student_dictionary)
                # Add to the list
                all_students.append(cur_student_instance)
            return all_students

    @classmethod
    def grab_one_student_with_teachers(cls, data):
        query = """
        SELECT * FROM students 
        LEFT JOIN students_teachers
        ON students.id = students_teachers.student_id
        LEFT JOIN teachers
        ON teachers.id = students_teachers.teacher_id
        WHERE students.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        else:
            # Create the Student class instance
            this_student_instance = cls(results[0])
            if results[0]["teachers.id"] != None: # At least one teacher is found
                # Loop through each teacher dictionary
                for current_teacher_dictionary in results:
                    # Create the Teacher class instance
                    teacher_instance = teacher.Teacher({
                        "id": current_teacher_dictionary["teachers.id"],
                        "first_name": current_teacher_dictionary["teachers.first_name"],
                        "last_name": current_teacher_dictionary["teachers.last_name"],
                        "email": current_teacher_dictionary["teachers.email"],
                        "subject": current_teacher_dictionary["subject"],
                        "is_tenured": current_teacher_dictionary["is_tenured"],
                        "created_at": current_teacher_dictionary["teachers.created_at"],
                        "updated_at": current_teacher_dictionary["teachers.updated_at"],
                    })
                    teacher_instance.semester = current_teacher_dictionary["semester"] # Tie the semester in
                    this_student_instance.teachers.append(teacher_instance)
            return this_student_instance

    @classmethod
    def add_teacher_to_student(cls,data):
        query = """
        INSERT INTO students_teachers
        (semester, student_id, teacher_id)
        VALUES 
        (%(semester)s, %(student_id)s, %(teacher_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_students_not_taught_by_teacher(cls, data):
        query = """
        SELECT * FROM students 
        WHERE students.id 
        NOT IN 
        (SELECT student_id FROM students_teachers WHERE teacher_id = %(id)s);
        """
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) == 0:
            return []
        else:
            all_students = []
            for cur_student_dictionary in results:
                # Create the Student
                cur_student_instance = cls(cur_student_dictionary)
                # Add to the list
                all_students.append(cur_student_instance)
            return all_students

    @classmethod
    def remove_teacher_from_student(cls,data):
        query = """
        DELETE FROM students_teachers
        WHERE student_id = %(student_id)s AND teacher_id = %(teacher_id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def remove_student(cls, data):
        query = """
        DELETE FROM students WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)