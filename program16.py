class student:
    roll = ""
    cgpa =""

    def display(self):
        print(f"roll:{self.roll},cgpa: {self.cgpa}")


# print(isinstance(mehedi,student))
mehedi = student()
mehedi.roll= "324"
mehedi.cgpa= "2.3"
mehedi.display()

korim = student()
korim.roll= "44"
korim.cgpa= "4.3"
korim.display()
