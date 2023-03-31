

class student:
    Schn="Python"

    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln

    def getnm(self):
        print("My name is ",self.fn , self.ln)
        print("I study at ",self.Schn)
        print("I study at ",self.Schn,"Statring at",self.at,"End at",self.lt)

    @classmethod
    def getschool(cls,at,lt):
        # print("My name is "self.fs , self.ln)
        cls.at=at
        cls.lt=lt
        print("I study at ",cls.Schn,"Statring at",cls.at,"End at",cls.lt)


# ob1=student("Sushant","Jadhav")
# student.getschool()
ob2=student("Sushant","Jadhav")
# ob2.getnm()
ob2.getschool(10,12)
