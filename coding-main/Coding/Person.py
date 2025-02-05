class Person: 
    def __init___(self, Firstname,secondname,fullname,age):

        self.Firstname = Firstname 
        self.secondname = secondname 
        self.fullname = Firstname + " " + secondname 
        self.age = age 

        def talk(self):
            print(f"Hello my name is{self.fullname} and I am {self.age} years old")


Martin = Person("Martin","Metodiev","19")
Martin.talk()




