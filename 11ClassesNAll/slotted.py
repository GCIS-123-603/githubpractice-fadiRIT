class GCIS123:
    __slots__=('course','fee')

    def __init__(self):
        self.course="GCIS123 Python"
        self.fee=4000


obj1=GCIS123()

print(obj1.__slots__)
print(str(obj1.course)+str(obj1.fee))   
