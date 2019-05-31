import random, sys

firstnames = ['Bobby','James','Kevin','Lisa','Mary','Diane','Joan','Garret','Sila','Gordon','Michael','David']
lastnames = ['Johnson','Hunt','Katz','Marley','Roberson','Smith']

class Person():
    population = 0
    
    def __init__(self, first = None, last = None, age = None):
        if(first and last and age):        #overloaded constructors
            self.first = str(first)
            self.last = str(last)
            self.name = str(first+' '+last)
            self.age = int(age)
        elif(first and last):
            self.first = str(first)
            self.last = str(last)
            self.name = str(first+' '+last)
            self.age = random.randint(1,86)
        else:
            self.first = firstnames[random.randint(0,len(firstnames)-1)]
            self.last = lastnames[random.randint(0,len(lastnames)-1)]
            self.name = self.first+' '+self.last
            self.age = random.randint(1,86)
        Person.population += 1
    
    def introduce(self):
        print('Hi, my name is '+self.first+' of house '+self.last+' and I am '+str(self.age)+' years old.')
    
    def census(self):
        print('There are '+str(Person.population)+' people in this town')
    
    def rename_first(self,n):
        self.first = n
    
    def rename_last(self,n):
        self.last = n
    
    def grow(self):
        self.age += 1

    def die(self):
        print(self.name+' died.')
        Person.population -=1

    def joust(self, Person):
        print(self.name+' challenged '+Person.name+' to a joust!')
        outcome = random.randint(0,2)
        if(outcome == 1):
            print(self.first+' of house '+self.last+': I win!')
            Person.die()
        else:
            print(Person.first+' of house '+Person.last+': I win!')
            self.die()

def handler(n):
    people = []
    print('generating town')
    for i in range(int(n)):
        p = Person()
        p.introduce()
        people.append(p)
    """p = Person('Bobby','Johnson')
    p.introduce()
    people.append(p)"""     #test for custom constructor
    people[0].census()
    people[0].joust(people[random.randint(1,num)])

num = random.randint(1,101)
handler(num)



"""
if len(sys.argv) > 1:
    handler(int(sys.argv[1])
else:
    handler(5)
"""
