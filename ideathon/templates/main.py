from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app=Flask(__name__)
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
def __init__(self, name, position, event):
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
def __init__(self, name, event):
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
def __init__(self, name, course, marks):
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
    return render_template("index.html")

@app.route("/resume", methods=['GET'])
def resume():
    return render_template("templateoh.html",link1="",link2="",link3="",link4="")

@app.route("/certificate", methods=['GET'])
def certificate():
    return render_template("",link1="",link2="")


@app.route("/resume/<string:template>", methods=['POST'])
def templateNumber(template):
    if(template=='template1'):
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        CareerObjective = request.json['CareerObjective']
        Education = request.json['Education']
        Skills = request.json['Skills']
    
        new_user = User(name, email, phone, CareerObjective, Education, Skills)

        db.session.add(new_user)
        db.session.commit()
        return render_template("")

    elif(template=='template2'):
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        CareerObjective = request.json['CareerObjective']
        Education = request.json['Education']
        Skills = request.json['Skills']
    
        new_user = User(name, email, phone, CareerObjective, Education, Skills)

        db.session.add(new_user)
        db.session.commit()
      return render_template("result.html",result = result)

    elif(template=='template3'):
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        CareerObjective = request.json['CareerObjective']
        Education = request.json['Education']
        Skills = request.json['Skills']
    
        new_user = User(name, email, phone, CareerObjective, Education, Skills)

        db.session.add(new_user)
        db.session.commit()
        return render_template("result.html",result = result)
   
        
@app.route("/resume/template1/finish",methods=["GET"])
def fin():
    return render_template("dummy.html", name=User.query.get(name), email = User.query.get(email), phone = User.query.get(phone), CareerObjective= User.query.get(CareerObjective), Skills= User.query.get(Skills))

@app.route("/resume/template2/finish",methods=["GET"])
def fin1():
    return render_template("dummy2.html", name=User.query.get(name), email = User.query.get(email), phone = User.query.get(phone), CareerObjective= User.query.get(CareerObjective), Skills= User.query.get(Skills))


@app.route("/resume/template3/finish",methods=["GET"])
def fin2():
    return render_template("dummy3.html", name=User.query.get(name), email = User.query.get(email), phone = User.query.get(phone), CareerObjective= User.query.get(CareerObjective), Skills= User.query.get(Skills))

@app.route("/certificate/<string:template>", methods=['POST'])
def CertNumber(template):
    if(template==template1):
        name = request.json['name']
        position = request.json['position']
        event = request.json['event']
        
        new_user = User2(name, position, event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert1.html")

    elif(name==template2):
        name = request.json['name']
        position = request.json['position']
        event = request.json['event']
        
        new_user = User2(name, position, event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert1.html")
        return render_template("cert2.html")

@app.route("/certificate/template1/<string:style>", methods=['PUT'])
def styleOfCertificate(style):
    if (style=='styleMerit'):
        name = request.json['name']
        position = request.json['position']
        event = request.json['event']
        
        new_user = User2(name, position, event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert1form.html")
    elif (style=='styleParticipation'):
        name = request.json['name']
        event = request.json['event']
        new_user = User3(name, event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert2form.html")
    elif (style=='styleCourse'):
        name = request.json['name']
        course = request.json['course']
        marks = request.json['marks']
        new_user = User4(name, course, marks)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert3form.html")
        
@app.route("/certificate/template2/<string:style>", methods=['PUT'])
def styleOfCertificate2(style):
    if (style=='styleMerit'):
        name = request.json['name']
        position = request.json['position']
        event = request.json['event']
        
        new_user = User2(name, position, event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert1form.html")
    elif (style=='styleParticipation'):
        name = request.json['name']
        event = request.json['event']
        new_user = User3(name, event)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert2form.html")
    elif (style=='styleCourse'):
        name = request.json['name']
        course = request.json['course']
        marks = request.json['marks']
        new_user = User4(name, course, marks)

        db.session.add(new_user)
        db.session.commit()
        return render_template("cert3form.html")


@app.route("/certificate/template1/styleMerit/finish", methods=['GET'])
def finishMerit():
    return render_template("", name=User2.query.get(name),position= User2.query.get(position), event=User2.query.get(event))

@app.route("/certificate/template1/styleParticipation/finish", methods=['GET'])
def finishParticipation():
    return render_template("", name= User3.query.get(name), event=User3.query.get(event))

@app.route("/certificate/template1/styleCourse/finish", methods=['GET'])
def finishCourse():
    return render_template("", name= User4.query.get(name), course=User4.query.get(course), marks=User2.query.get(marks))

@app.route("/certificate/template2/styleMerit/finish", methods=['GET'])
def finishMerit2():
    return render_template("", name=User2.query.get(name), position=User2.query.get(position),event= User2.query.get(event))

@app.route("/certificate/template2/styleParticipation/finish", methods=['GET'])
def finishParticipation2():
    return render_template("",name= User3.query.get(name), event=User3.query.get(event))

@app.route("/certificate/template2/styleCourse/finish", methods=['GET'])
def finishCourse2():
    return render_template("", name=User4.query.get(name), course=User4.query.get(course), marks=User2.query.get(marks))



if __name__=='__main__':
    app.run()