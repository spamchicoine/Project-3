from Movie import *
import random
import sys

class MovieList:
    def __init__(self,file):
        text = open(file) # Opens file in read mode
        self.__list =[]
        for n in text: # Appands a movie object using the data from the text file to our list
            data = n.split('\n')[0].split(';') # Splits each text line in useful data
            self.__list.append(Movie(data[0],data[1],data[2]))
    
    def getSize(self):
        return len(self.__list)
    
    def binarySearch(self,id): # Binary search algorithm that finds the inputted id
        lower = 0
        upper = len(self.__list)-1
        while lower <= upper:
            middle = lower + (upper - lower)//2 # Updates middle index
            if int(self.__list[middle].getID()) == id:   # Checks if middle index matches id searched for
                return self.__list[middle]
            
            elif int(self.__list[middle].getID()) < id: # Adjusts lower bound if item at middle index is less than id searched for
                lower = middle + 1
            
            elif int(self.__list[middle].getID()) > id: # Adjusts upper bound if item at middle index is greater than id searched for
                upper = middle - 1

        return 'Movies not found'
    
    def shuffle(self): # Shuffles inputted list
        for i in range(len(self.__list)-1,0,-1):
            index = random.randint(0,i) # Creates a random index
            self.__list[i],self.__list[index] = self.__list[index],self.__list[i] # Swap values using random index

    def save(self,filename): # Saves list data to a new file named by input
        write = open(filename,'w') # Opens file of filename in write mode
        for i in self.__list:
            write.write(str(i)+'\n') # Writes each list item on each line of the text line

    def recDisplayOrder(self,current):
        if current is not None:
            self.recDisplayOrder(current.left)
            print(current.data,end="")
            self.recDisplayOrder(current.right)

    def displayInOrder(self):
        print('display in order %s items'%(self.getSize()))
        self.recDisplayOrder(self.root)
        print()