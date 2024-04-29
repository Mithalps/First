from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def show_students():
        #Example list of names and ages
        students=[
            {"name" :"Moonyo","grade": 70},
            {"name" :"porthimo","grade": 70},
            {"name" :"MOGHONO","grade": 65},
            {"name" :"sanjana","grade": 70},
            {"name" :"prajna","grade": 80},
            {"name" :"NISHO","grade": 72},
        ]
        passing_grade=80
        return render_template('grade.html', students=students, passing_grade=passing_grade)
app.run(debug=True) 