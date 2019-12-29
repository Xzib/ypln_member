from app import db, RegisteredMember, UserInfo

db.create_all()

zohaib = RegisteredMember('zohaib','zohaib@gmail.com','xzib','1234',21345)
owais = RegisteredMember('owais','owais@gmail.com','vesi','1234',21345)

db.session.add_all([zohaib,owais])
db.session.commit()

#check
print(RegisteredMember.query.all())

owais = RegisteredMember.query.filter_by(fullname='owais').first()
print(owais)

#create userinfo object
zohaib_info = UserInfo("hi i am zohaib, I am an engineer", zohaib.id)
owais_info = UserInfo("hi i am owais, I am a chemist", owais.id)

db.session.add_all([zohaib_info,owais_info])
db.session.commit()
 
owais = RegisteredMember.query.filter_by(fullname='owais').first()
print(owais)