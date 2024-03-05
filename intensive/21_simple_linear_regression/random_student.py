def random_student():
    '''
        Randomly select a student from a list of students in the class.

        Input(s): no input.

        Return(s): a randomly chosen student name.
    '''

    import random

    student_list = [
        'Mark', 'Daniel',
        'Charles', 'Quentin',
        'Andrew', 'Adam',
        'Paola', 'Luisa',
        'Andrea', 'Nicole',
        'Emily', 'Julie',
        'Leonardo', 'Noe',
        'Omar', 'Kevin',
        'Matthew', 'Patrick',
        'Jonathan', 'Aaron']

    student_selected = random.choice(student_list)
    print(f'The lucky student is: {student_selected}')
