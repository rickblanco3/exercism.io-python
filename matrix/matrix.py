class Matrix(object):
    def __init__(self, string):
        self.rows = [map(int, row.split(' ')) for row in string.split('\n')]
        self.columns = [[row[i] for row in self.rows] for i in range(len(self.rows[0]))] 
