from Movie import *
import MovieList

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
        nodes = open(file)
        for n in nodes: #Inserts the data from each line of the text file as a movie object node
            data = n.split('\n')[0].split(';') # Gets useful data from each text line
            self.insert(Movie(int(data[0]),int(data[1]),data[2])) # Inserts movie object as a node
    
    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.root is None
    
    def insert(self,movie): 
        newNode = Node(movie)
        if self.__size == 0: #Corner case if BST is empty
            self.root = newNode
            self.__size += 1
        else:
            self.recInsert(self.root,newNode) # Begins recursive insertion

    def recInsert(self,current,new): # Recursively compares data to insert with left and right nodes
        if new.movie.getID()<current.movie.getID(): # Search left
            if current.left is None:
                current.left=new    # Insert node
                current.left.index = 2*current.index+1
                self.__size+=1
            else:
                self.recInsert(current.left,new)
        elif new.movie.getID()>=current.movie.getID(): # Search right
            if current.right is None:
                current.right=new # Insert node
                current.right.index = 2*current.index+2
                self.__size+=1
            else:
                self.recInsert(current.right,new)

    def search(self,id): # Searches BST for given ID
        if self.isEmpty(): # Corner case if BST is empty
            return None
        else:
            node=self.recSearch(self.root,id) # Starts recursive searching
        return node
    
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

    def recExtract(self,current,key,file):
        if current is not None:
            self.recExtract(current.left,key,file)
            if key.lower() in [title.lower() for title in current.movie.getTitle().split()]: file.write('%s;%s;%s\n'%(current.movie.getID(),current.movie.getYear(),current.movie.getTitle()))
            self.recExtract(current.right,key,file)

    def extractListInOrder(self,key):
        f1 = open('MovieListTemp.txt','w')
        self.recExtract(self.root,key,f1)
        f1.close
        f2 = open('MovieListTemp.txt')
        print('Print all lines in f2:')
        for line in f2:
            print(line)
        f2.close()
        return MovieList.MovieList('MovieListTemp.txt')

moviesbst = MovieBST('Movies.txt')