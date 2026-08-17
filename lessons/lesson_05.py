class Employee:
    def __init__(self, name, position, experience):
        self.name = name
        self.position = position
        self.experience = experience

    def print_info(self):
        print(f"\nName: {self.name}")
        print(f"Position: {self.position}")
        print(f"Expirience: {self.experience}\n")




employee1 = Employee("Iryna", "QA Engineer", "5 years")
employee2 = Employee("Sasha", "Dev Engineer", "3 years")
employee1.print_info()
employee2.print_info()
