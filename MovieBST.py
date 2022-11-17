from Movie import *
import MovieList
import numpy as num
import Queue as Q
from tkinter import *

# Nathan Robinson
# Sam Chicoine


class Node():

    def __init__(self,movie):
        self.movie = movie
        self.left = None
        self.right = None
        self.index=0

    def __str__(self): # Overloads str() so Node returns the movie data
        return str(self.movie)

class MovieBST():
    
    def __init__(self,file):
        self.root = None
        self.__size = 0
        self.__maxindex = 0
        nodes = open(file)
        for n in nodes: #Inserts the data from each line of the text file as a movie object node
            data = n.split('\n')[0].split(';') # Gets useful data from each text line
            self.insert(Movie(int(data[0]),int(data[1]),data[2])) # Inserts movie object as a node
    
    # Method to return size of MovieBST
    # Input: self
    # Output: returns self.__size
    def getSize(self):
        return self.__size

    # Method to return if MovieBST is empty
    # Input: sef
    # Output: True or False
    def isEmpty(self):
        return self.root is None
    
    # Method to insert new node using recursice auxillary method
    # Input: self, 'movie' the movie object to be inserted
    # Output: sets self.__root to be the new node if BST is empty, otherwise calls auxillary method
    def insert(self,movie): 
        newNode = Node(movie)
        if self.__size == 0: #Corner case if BST is empty
            self.root = newNode
            self.__size += 1
        else:
            self.recInsert(self.root,newNode) # Begins recursive insertion

    # Recursive auxillary method for insert
    # Input: self, 'current' the current node, and 'new' the node to be inserted
    # Output: increases self.__size, and adds new node to corresponding index
    def recInsert(self,current,new): 
        if new.movie.getID()<current.movie.getID(): # Search left
            if current.left is None:
                current.left=new    # Insert node
                current.left.index = 2*current.index+1
                if current.left.index > self.__maxindex:
                    self.__maxindex = current.left.index
                self.__size+=1
            else:
                self.recInsert(current.left,new)
        elif new.movie.getID()>=current.movie.getID(): # Search right
            if current.right is None:
                current.right=new # Insert node
                current.right.index = 2*current.index+2
                if current.right.index > self.__maxindex:
                    self.__maxindex = current.right.index
                self.__size+=1
            else:
                self.recInsert(current.right,new)

    # Method to search MovieBST for given ID using auxillary recursive method
    # Input: self, and 'id' the ID to search for
    # Output: returns the node of movie with given ID, or none
    def search(self,id):
        if self.isEmpty(): # Corner case if BST is empty
            return None
        else:
            node=self.recSearch(self.root,id) # Starts recursive searching
        return node
    
    # Recursive auxillary method for search
    # Input: self, 'current' the current node, and 'id' the ID to search for
    # Output: returns the node of the movie with given ID, or none if not found
    def recSearch(self,current,id):
        if current is None: return None # ID not found and reached end of BST
        if id<current.movie.getID(): # Searches left subtree if ID is smaller than current
            temp=self.recSearch(current.left,id)
        elif id>current.movie.getID(): # Searches right subtree if ID is greater than current
            temp=self.recSearch(current.right,id)
        else:
            temp=current # ID found
        return temp

    # Recursive auxillary function for displayInOrder
    # Input: self and 'current' (the current node)
    # Output: moves through the tree recursively and prints each movie in the tree
    def recDisplay(self, current):
        if current is not None:
            self.recDisplay(current.left)
            print(current.movie)
            self.recDisplay(current.right)

    # Function to display contents of the tree of movies sorted by ID
    # Input: self
    # Output: Prints number of items being displayed
    def displayInOrder(self):
        print('Display in order %s items by ID'%(self.__size))
        self.recDisplay(self.root)
        print()

    # Revursive auxillary method for show
    # Input: self, 'current' the current node, and 'indentSTR' the string to be printed before the data, creating an indent
    # Output: moves through tree recursively, printing movie ID and index
    def recShow(self,current,indentSTR):
        if current is not None:
            self.recShow(current.right,indentSTR+"\t")
            print(indentSTR+str(current.movie.getID())+'(%s)'%(current.index))
            self.recShow(current.left,indentSTR+"\t")

    # Method to display BSTree
    # Input: self
    # Output: prints beginning line and calls recursive auxillary function
    def show(self):
        print('The BSTree looks like:')
        self.recShow(self.root,"")

    # Recursive auxillary method for extractListInOrder
    # Input: self, 'current' the current node, 'key' the keyword to search for, and 'file' the file to write all found movies to
    # Output: writes all movies with key in their title to given file
    def recExtract(self,current,key,file):
        if current is not None:
            self.recExtract(current.left,key,file)
            if key.lower() in [title.lower() for title in current.movie.getTitle().split()]: file.write('%s;%s;%s\n'%(current.movie.getID(),current.movie.getYear(),current.movie.getTitle()))
            self.recExtract(current.right,key,file)

    # Method to return a MovieList of movies with the given key in their title
    # Input: self and 'key' the keyword to search for
    # Output: MovieList object containing the movies, also creates 'MovieListTemp.txt' to create the MovieList object
    def extractListInOrder(self,key):
        f1 = open('MovieListTemp.txt','w')
        self.recExtract(self.root,key,f1)
        f1.close()
        return MovieList.MovieList('MovieListTemp.txt')
    
    # Method to get stored max index
    # Input: bst object
    # Output: Max index attribute of input
    def getMaxIndex(self):
        return self.__maxindex
    
    # Method to return the max level of a bst object
    # Input: bst object
    # Output: Returns bst level
    def getMaxLevel(self):
        index = self.__maxindex+1
        while num.log2(index)%1 != 0:
            index += 1
        return int(num.log2(index))-1
    
    # Method to display the movie bst in level order
    # Input: bst object to display
    # Output: Prints the objects as it dequeques and return the list representation of the bst
    def displayLevelOrder(self):
        list = [None]*(2**(self.getMaxLevel()+1)) # Initialize list of Nones to be our list representation of a bst
        queque = Q.Queue(self.getMaxIndex()+1) # Initialize our queque
        root = self.root
        queque.enqueue(root)
        while queque.isEmpty() is False: # Iterates through our nodes
            print(queque.peekFront())
            front = queque.dequeue() # Pops first node in queque
            list[front.index]=front # Sets popped node to corrent position in list representation of bst
            if front.left: # Checks for left child of popped node
                queque.enqueue(front.left)  
            if front.right: # Checks for right child of popped node
                queque.enqueue(front.right)
        return list
    
    # Static method to take a list representation of a bst and turn it into a tree diagram using tkinter
    # Input: List representation of bst
    # Output: Tkinter diagram of bst with used nodes colored blue
    @staticmethod 
    def plotBST(list):
        index = len(list)
        while num.log2(index)%1 != 0:
            index += 1
        level = int(num.log2(index))
        tk = Tk()
        cwidth = (level**2)*30
        cheight = level*30+25
        canvas = Canvas(tk,width = cwidth,height = cheight)
        canvas.pack()
        clevel = 0
        index = 0
        xylist = []
        for i in range(0,level): # Iterates through each level of the bst
            clevel += 1
            x = cwidth/(2**clevel)
            y = clevel*30
            for j in range(0,2**(clevel-1)): # Iterates through the nodes at each level
                xylist += [[x,y]]
                if list[index] is not None: # Checks if current node is not None, is so node is blue
                    canvas.create_oval(x-5,y-5,x+5,y+5,fill='blue')
                    if list[(index-1)//2] is not None: # Checks if parent is not none if so line between is blue
                        canvas.create_line(xylist[(index-1)//2][0],xylist[(index-1)//2][1],xylist[index][0],xylist[index][1],fill = 'blue')
                    else:   # Else line bewtween is gray
                        canvas.create_line(xylist[(index-1)//2][0],xylist[(index-1)//2][1],xylist[index][0],xylist[index][1],fill = 'gray')
                else: # Else node is gray
                    canvas.create_oval(x-5,y-5,x+5,y+5,fill='gray')
                    canvas.create_line(xylist[(index-1)//2][0],xylist[(index-1)//2][1],xylist[index][0],xylist[index][1],fill = 'gray')

                index += 1
                x += cwidth/(2**(clevel-1))
        tk.mainloop()




moviesbst = MovieBST('Movies.txt')