from Movie import *
import random
import sys

# Nathan Robinson
# Sam Chicoine

class MovieList:
    def __init__(self,file):
        text = open(file) # Opens file in read mode
        self.__list =[]
        for n in text: # Appands a movie object using the data from the text file to our list
            data = n.split('\n')[0].split(';') # Splits each text line in useful data
            self.__list.append(Movie(data[0],data[1],data[2]))
    
    # Method to return size of the MovieList
    # Input: self
    # Output: return length of self.__list
    def getSize(self):
        return len(self.__list)
    
    # Method to use binary search to search the MovieList for a given ID
    # Input: self, and 'id' the ID number to search for
    # Output: return movie with the given ID, or 'movies not found'
    def binarySearch(self,id): 
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
    
    # Method to shuffle the MovieList
    # Input: self
    # Output: changes indexes of the movies in MovieList
    def shuffle(self): 
        for i in range(len(self.__list)-1,0,-1):
            index = random.randint(0,i) # Creates a random index
            self.__list[i],self.__list[index] = self.__list[index],self.__list[i] # Swap values using random index

    # Method to save the MovieList to a given filename
    # Input: self, and 'filename' the name of the file to write the list to
    # Output: creates new file with 'filename' containing the MovieList
    def save(self,filename): 
        write = open(filename,'w') # Opens file of filename in write mode
        for i in self.__list:
            write.write(str(i)+'\n') # Writes each list item on each line of the text line

    # Recursive auxillary method for displayInOrder
    # Input: self and 'current' the current node
    # Output: prints the MovieList in order
    def recDisplayOrder(self,current):
        if current is not None:
            self.recDisplayOrder(current.left)
            print(current.data,end="")
            self.recDisplayOrder(current.right)

    # Method to display the MovieList in order using auxillary recursive method
    # Input: self
    # Output: prints initial statement and blank line after list
    def displayInOrder(self):
        print('display in order %s items'%(self.getSize()))
        self.recDisplayOrder(self.root)
        print()
    
    # Method to dispay the MovieList
    # Input: self
    # Output: prints the MovieList
    def display(self):
        for item in self.__list:
            print(item)