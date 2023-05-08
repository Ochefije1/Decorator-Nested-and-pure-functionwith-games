from activity_decorator_busary_linking_page import isIndigene


@isIndigene('state':'Rivers', 'cgpa':4.0, year=0, Amount=50000)
def payBusary(student):
    if student.get('isPaid'):
        return student
    return


students = [
    {'name':'Udenta Amaka', 'cgpa':4.2, 'dept':'Fine Arts', 'level':2, 'state':'Abia'},
    {'name':'Adeniyi Adeleke', 'cgpa':3.9, 'dept':'Fine Arts', 'level':2, 'state':'Lagos'},
    {'name':'TAmuno Alero', 'cgpa':3.2, 'dept':'Fine Arts', 'level':2, 'state':'Rivers'},
    {'name':'Obani Olanma', 'cgpa':4.8, 'dept':'Fine Arts', 'level':3, 'state':'Rivers'},
    {'name':'Udiniyi Noni', 'cgpa':3.0, 'dept':'Fine Arts', 'level':2, 'state':'Lagos'}
]

for student in students:
    paidStudents = payBusary(student)
    print(paidStudents)
