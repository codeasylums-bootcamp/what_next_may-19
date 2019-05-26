from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app=Flask(__name__,static_url_path='/static', static_folder='templates')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(60), unique=True)
    CareerObjective = db.Column(db.String(120), unique=True)
    Education = db.Column(db.String(80), unique=True)
    Skills= db.Column(db.String(80), unique=True)


def __init__(self, name, email, phone, CareerObjective, Education, Skills):
    self.name = name
    self.email = email
    self.phone = phone
    self.CareerObjective = CareerObjective
    self.Education = Education
    self.Skills = Skills

class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email', 'phone', 'CareerObjective', 'Education', 'Skills')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    position = db.Column(db.String(120), unique=True)
    event = db.Column(db.String(120), unique=True)
def __init3__(self, name, position, event):
    self.name = name
    self.position = position
    self.event = event
class User2Schema(ma.Schema):
    class Meta1:
        fields = ('name', 'position', 'event')


user_schema2 = User2Schema()
users_schema2 = User2Schema(many=True)


class User3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    event = db.Column(db.String(120), unique=True)
def __init1__(self, name, event):
    self.name = name
    self.event = event
class User3Schema(ma.Schema):
    class Meta2:
         fields = ('name', 'event')


user_schema3 = User3Schema()
users_schema3 = User3Schema(many=True)

class User4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    course = db.Column(db.String(120), unique=True)
    marks = db.Column(db.String(20), unique= False)
def __init2__(self, name, course, marks):
    self.name = name
    self.course = course
    self.marks = marks
class User4Schema(ma.Schema):
    class Meta3:
        fields = ('name', 'course','marks')


user_schema4 = User4Schema()
users_schema4 = User4Schema(many=True)


@app.route("/", methods=['GET'])
def main():
    return render_template("homepage.html")

@app.route("/resume", methods=['GET'])
def resume():
    return render_template("templateoh.html")

@app.route("/certificate", methods=['GET'])
def certificate():
    return render_template("temp.html")


@app.route("/resume/<string:template>", methods=['GET'])
def templateNumber(template):
    if(template=='template1'):
        
        return render_template("")

    elif(template=='template2'):
       
        return render_template("homepage.html")

    elif(template=='template3'):
        
        return render_template("result.html")
   
        
@app.route("/resume/template1/finish",methods=['GET','POST'])
def fin():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        CareerObjective = request.form['CareerObjective']
        Education = request.form['Education']
        Skills = request.form['Skills']
    
        new_user = User(name, email, phone, CareerObjective, Education, Skills)

        db.session.add(new_user)
        db.session.commit()
        return render_template("dummy.html", name, email, phone, CareerObjective,Education, Skills)
    else:
        return render_template("dummy.html",name, email, phone, CareerObjective,Education, Skills)


@app.route("/resume/template2/finish",methods=['GET','POST'])
def fin1():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        CareerObjective = request.form['CareerObjective']
        Education = request.form['Education']
        Skills = request.form['Skills']
    
        new_user = User(name=name, email=email,phone= phone,CareerObjective= CareerObjective, Education=Education, Skills=Skills)

        db.session.add(new_user)
        db.session.commit()
        return render_template("dummy2.html", name, email, phone, CareerObjective, Education, Skills)
    else:
        return render_template("dummy.html",name, email, phone, CareerObjective, Education, Skills)

@app.route("/resume/template3/finish",methods=["GET"])
def fin2():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        CareerObjective = request.form['CareerObjective']
        Education = request.form['Education']
        Skills = request.form['Skills']
    
        new_user = User(name=name, email=email,phone=phone, CareerObjective=CareerObjective, Education=Education, Skills=Skills)

        db.session.add(new_user)
        db.session.commit()
        return render_template("dummy2.html",name, email, phone, CareerObjective, Education, Skills)
    else:
        return render_template("dummy.html",name, email, phone, CareerObjective, Education, Skills)
    


@app.route("/certificate/<string:style>", methods=['GET'])
def styleOfCertificate(style):
    if (style=='styleMerit'):
        return render_template("formmerit.html")
    elif (style=='styleParticipation'):
        return render_template("formpart.html")
    elif (style=='styleCourse'):
        return render_template("formcourse.html")
    else:
        return ("homepage.html")

@app.route("/certificate/styleMerit/finish", methods=['GET','POST'])
def finishMerit():
    if request.method=='POST':
        name = request.form['name']
        position = request.form['position']
        event = request.form['event']
        
        new_user = User2(name=name, position=position, event=event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("merittem.html", name=name, position=position, event=event)
    else:
        return render_template("merittem.html", name, position, event)

@app.route("/certificate/styleParticipation/finish", methods=['GET','POST'])
def finishParticipation():
    if request.method=='POST':
        name = request.form['name']
        event = request.form['event']
        
        new_user = User3(name=name, event=event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("participation.html",name=name, event=event)
    else:
        return render_template("participation.html", name, event)


@app.route("/certificate/styleCourse/finish", methods=['GET','POST'])
def finishCourse():
    if request.method=='POST':
        name = request.form['name']
        course = request.form['course']
        marks = request.form['marks']
        
        new_user = User4(name=name, course=course, marks=marks)

        db.session.add(new_user)
        db.session.commit()
        return render_template("coursetem.html", name=name, course=course, marks=marks)
    else:
        return render_template("coursetem.html", name, course, marks)



if __name__=='__main__':
    app.run()