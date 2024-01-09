class Person:
    def __init__(self, name, age, gender, occupation, job, farbaoci,):
     self.name = name
     self.age = age
     self.gender = gender
     self.occupation = occupation
     self._job = job
     self.__farbaoci = farbaoci

    def location(self):
        print(f"{self.name} sa nachadza v {self.occupation}")

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov a pracujem ako {self._job}")
    def zostarni(self, kolko):
        age = self.age + kolko
        self.age = age
        print(f"Novy vek je {age}")
patrik = Person("Patrik", 30, "muz", "Bratislava", "lekar","modre")
dalibor = Person("Dalibor", 27, "muz", "Bratislava", "doktor", "hnede")
patrik.name = "Milan"
patrik.pozdrav()
patrik.zostarni(10)
dalibor.location()

print(patrik.age)
