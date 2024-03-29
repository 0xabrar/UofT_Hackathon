#Abrar Hussain

from tkinter import *
from tkinter import ttk
from graphics_interface import SortingGraphics
from algorithms import *
from threading import Thread


class Controller():
    '''
    A class which acts as the main controller that switches between different algorithms. Also implements the overall graphical interface of having a Canvas and buttons.
    
    operations:
        - previous_algorithm: start the previous algorithm
        - next_algorithm: start the next algorithm
        - add_algorithms: will add all of the algorithms classes into a collection
        
    attributes:
        - algorithm_classes: list that keeps track of all the different algorithms
    
    '''
    
    def add_algorithms(self: 'Controller') -> None:
            '''
            Will add in all of the algorithms into a collection.
            '''
            #used to maintain the instances of different algorithm classes
            self.algorithm_classes = []  
            #maintain string names of the different algorithms
            self.algorithm_names = []
            
            self.algorithm_classes.append(SelectionSort)
            self.algorithm_classes.append(InsertionSort)
            self.algorithm_classes.append(BubbleSort)
            self.algorithm_classes.append(HeapSort)
            
            self.algorithm_names.append('Selection Sort')
            self.algorithm_names.append('Insertion Sort')
            self.algorithm_names.append('Bubble Sort')      
            self.algorithm_names.append('Heap Sort')
            
            #used to maintain information about current algorithm
            self.current_algorithm_index = 0
            
    def previous_algorithm(self: 'Controller', canvas: Canvas) -> None:
        '''
        Starts the processing of the previous algorithm in the algorithm collection.
        '''
        name = ttk.Label(text = self.algorithm_names[self.current_algorithm_index])
        name.grid(row = 2, column = 3)         
        
        self.algorithm_classes[self.current_algorithm_index](canvas)
        #return to last class if past beginning of list
        self.current_algorithm_index = (self.current_algorithm_index - 1) % len(self.algorithm_classes)
        
    def next_algorithm(self: 'Controller', canvas: Canvas) -> None:
        '''
        Starts the processing of the next algorithm in the algorithm collection.
        '''    
        if (self.algorithm == None):
            name = ttk.Label(text = self.algorithm_names[self.current_algorithm_index])
            name.grid(row = 2, column = 3) 
        
            self.algorithm_classes[self.current_algorithm_index](canvas)
            #return to first class if past end of list
            self.current_algorithm_index = (self.current_algorithm_index + 1) % len(self.algorithm_classes)
    
    def __init__(self: 'Controller') -> None:
        '''
        Create the initial canvas and button options and call for main executions.
        '''
        
        root = Tk()
        root.title("Graphing Algorithms")
        
        #used to keep track of multithreading
        self.funky = False
        
        #the canvas and buttons are initialized, as well as 'funky' checkbox
        canvas = Canvas(root, bg = 'white', width = 800, height = 600)
        previous_button = ttk.Button(root, text = "Previous", command = lambda: self.previous_algorithm(canvas))
        next_button = ttk.Button(root, text = "Next", command = lambda: self.next_algorithm(canvas)) 
     
        #canvas and buttons are organized onto screen, with canvas displayed and 
        # the two buttons centered under canvas
        canvas.grid(row = 0, column = 0, columnspan = 25)
        previous_button.grid(row = 2, column = 12)
        next_button.grid(row = 2, column = 13)   
        
        self.add_algorithms()
        #self.next_algorithm(canvas)	
        root.mainloop()
        
#Start the actual program.
controller = Controller()

