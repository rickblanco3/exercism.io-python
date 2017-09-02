class Garden(object):

    plant_names = {'C':'Clover','G':'Grass','R':'Radishes','V':'Violets'}

    def __init__(self,layout,students="Alice Bob Charlie David Eve Fred Ginny Harriey Ileana Joseph Kincaid Larry".split()):
        self._layout = layout.split() # split layout into a string list of length 2
        students.sort()               # students plant seeds by ascending name order
        self._students = students

    def plants(self,student_name):
        if student_name not in self._students:
            raise ValueError("Student not found.")
        # find where the student's plants start on each row
        idx = self._students.index(student_name) * 2
        # for each row in _layout, get the substring representing the student's plants
        return [self.plant_names[p] for row in self._layout for p in row[idx:idx+2]]

