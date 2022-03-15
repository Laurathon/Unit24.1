"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of departments
# d1 = Department(dept_code="mktg", dept_name="Marketing")
# d2 = Department(dept_code="acct", dept_name="Accounting")
# d3 = Department(dept_code="r&d",
#                 dept_name="Research and Development", phone="908-7878")
# d4 = Department(dept_code="sales", dept_name="Sales", phone="225-6912")
# d5 = Department(
#     dept_code="it", dept_name="Information Technology", phone="888-4562")

# db.session.add_all([d1, d2, d3, d4, d5])

# db.session.commit()

# # Make a bunch of employees

# river = Employee(name="River Bottom", state="NY", dept_code="mktg")
# summer = Employee(name="Summer Winter", state="OR", dept_code="mktg")
# joaquin = Employee(name="Joaquin Phoenix", dept_code="acct")
# octavia = Employee(name="Octavia Spencer", dept_code="r&d")
# larry = Employee(name="Larry David", dept_code="r&d", state="NY")
# kurt = Employee(name="Kurt Cobain", dept_code="it", state="WA")
# rain = Employee(name="Rain Phoenix", dept_code="it")

# db.session.add_all([river, summer, joaquin, octavia, larry, kurt, rain])

# db.session.commit()

Pet.query.delete()


# Add sample employees and departments
petOne = Pet(name='Angel', species='dog', photo_url='https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg', age=2, notes="very shy")
petTwo = Pet(name='Loki', species='bird', photo_url='data:image/jpeg;base64,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', age=1, notes="bites")
petThree = Pet(name='Jasmine', species='cat', photo_url='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&w=1000&q=80', age=4, notes="dislikes other animals")



db.session.add_all([petOne, petTwo, petThree])
db.session.commit()
