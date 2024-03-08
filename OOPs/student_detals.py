class student:
    clg = "IISER BHOPAL"

    def __init__(self,name,roll):
        self.roll = roll
        self.name = name
    
    def display(self):
        print("Name:",self.name)
        print("Roll-No:",self.roll)
        print("College:",student.clg)

student("Nirman","22223").display()
student("Swarnim","22344").display()