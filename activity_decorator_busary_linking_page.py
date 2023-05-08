


def isIndigene(state, year, amount):
    def inner(func):
        def wrapper(student):
            if state is None:
                if year is None:
                    student.update({'paid':amount, 'isPaid':True})
                elif student['level'] == year:
                        student.update({'paid':amount, 'isPaid':True})
            elif student['state'] == state:
                if year is None:
                    student.update({'paid':amount, 'isPaid':True})
                    if student['cgpa'] >= 4.0:
                        student['paid'] = amount * 2
                elif student['level'] == year:
                    student.update({'paid':amount, 'isPaid':True})
                    if student['cgpa'] >= 4.0:
                        student['paid'] = amount * 2                       
            return func(student)
        return wrapper
    return inner