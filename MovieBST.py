from Movie import *

class Node():

    def __init__(self,movie):
        self.movie = movie
        self.left = None
        self.right = None

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
                current.left=new # Insert node
                self.__size+=1
            else:
                self.recInsert(current.left,new)
        elif new.movie.getID()>=current.movie.getID(): # Search right
            if current.right is None:
                current.right=new # Insert node
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


moviesbst = MovieBST('Movies.txt')