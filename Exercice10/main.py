class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Mon nom est {self.name} et j'ai {self.age} ans.")


class Employee(Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        print(f"Mon nom est {self.name}, j'ai {self.age} ans. Mon salaire est de {self.salary}€")


person = Person("Wilfried", 44)
person.display_details()

employee = Employee("Jack", 46, 3500)
employee.display_details()
