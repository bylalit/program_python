class Students:
    marks = 10
    @classmethod
    def modify(cls, name):
        print(" {} scored {} marks" .format(name, cls.marks))
        
Students.modify("Snajay")
Students.modify("Ajay")