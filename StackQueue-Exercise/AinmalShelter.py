class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self,animal,type):
        if type =='Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) ==0:
            return "No cats available"
        else:
            cat = self.cats.pop(0)
            return cat
        
    def dequeueDog(self):
        if len(self.dogs) ==0:
            return "No cats available"
        else:
            dog = self.dogs.pop(0)
            return dog
    
    def dequeueAny(self):
        if len(self.cats) >0:
           return self.dequeueCat()
        else:
           return self.dequeueDog()

custQueue = AnimalShelter()

custQueue.enqueue(animal ='Cat1',type ='Cat')
custQueue.enqueue(animal ='Dog1',type ='Dog')
custQueue.enqueue(animal ='Cat2',type ='Cat')
custQueue.enqueue(animal ='Dog2',type ='Dog')
custQueue.enqueue(animal ='Cat3',type ='Cat')
custQueue.enqueue(animal ='Dog3',type ='Dog')
