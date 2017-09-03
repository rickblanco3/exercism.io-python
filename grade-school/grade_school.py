class School(object):
    def __init__(self,schoolname):
        self._schoolname = schoolname
        self._student_roll = {} #dict of type {grade_num:[student_a,student_b,...]}

    def grade(self,grade_num):
        '''
        returns a tuple with all students in a given grade.
        if no students in a given grade, return empty list
        '''
        return self._student_roll.get(grade_num, [])


    def add(self,student_name,grade_num):
        '''
        adds a student to a grade
        '''
        self._student_roll.setdefault(grade_num,[]).append(student_name)

    def sort(self):
        '''
        returns list of tuples containing all students, sorted by grade and name.
        '''
        return [(grade_num,tuple(sorted(self._student_roll[grade_num]))) for grade_num in sorted(self._student_roll)]
