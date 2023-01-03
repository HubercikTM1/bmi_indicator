class Person:
    def __init__(self, name, age, weight, height) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def introduction(self):
        print(f'Your name is {self.name}, you are {self.age} years old, you weight {self.weight} kg and you are {self.height} cm tall')
    
    def personBMI(self):
        bmi = self.weight/((self.height/100)**2)
        if(bmi<18.5):
            print(f'Your BMI is {bmi} and you are underweight!')
        elif(bmi>=18.5 and bmi<=25.0):
            print(f'Your BMI is {bmi} and you are at the correct weight!')
        elif(bmi>25.0 and bmi<=30.0):
            print(f'Your BMI is {bmi} and you are overweight!')
        else:
            print(f'Your BMI is {bmi} and you are obese!')

if __name__ == '__main__':
    hubert = Person('Hubert', 17, 77, 183)
    john = Person('John', 25, 100, 180)
    hubert.introduction()
    hubert.personBMI()
    john.introduction()
    john.personBMI()
