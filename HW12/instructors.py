from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_FILE = '/Users/nadik/Desktop/810/homework/810_repository.db'

@app.route('/instructors')
def instructors():

    query = """select i.cwid, i.name, i.dept, g.course, count(g.Student_CWID)as count
            from HW11_instructors i join HW11_grades g on i.cwid=g.Instructor_CWID
            group by i.cwid, i.name, i.dept, g.course"""

    db = sqlite3.connect(DB_FILE)
    results = db.execute(query)
    
    data = [{'cwid': cwid, 'name': name, 'dept': dept,
            'course': course, 'count': count} 
            for cwid, name, dept, course, count in results]

    db.close()
    return render_template('instructors.html', title='Stevens Repository',
                            table_title='Instructors', rows=data)
   

app.run(debug=True)