from tkinter import *
from tkinter import ttk
import random
from threading import Thread
import time
from graphics_interface import SortingGraphics

def create_random_list() -> list:
    '''
    Create a list with values from 1-50 inclusive, numbers non-repeating. Used
    for the different sorting algorithms.
    '''
    tracking = [] #used to determine what numbers are in random_list
    random_list = []
    while (len(random_list) < 50):
        number = random.randint(1, 50)
        if (number not in tracking):
            random_list.append(number)
            tracking.append(number)
    return random_list   

class InsertionSort():
    '''
    The class responsible for the implementation of the InsertionSort algorithm.
    Operates in n squared time worst-case
    '''
    
    def __init__(self: object, canvas: Canvas) -> None:
        unsorted_list = create_random_list()
        sorter = SortingGraphics(canvas, unsorted_list)
        
        #start a thread of InsertionSort
        t = Thread(target = self.insertion_sort, args = (sorter, canvas, unsorted_list))
        t.start()
    
    def insertion_sort(self: object, sorter: SortingGraphics, canvas: Canvas, unsorted_list: list) -> None:
        '''
        Perform InsertionSort and call the graphics_interface functions to display.
        '''
        for x in range(len(unsorted_list)):
            key = unsorted_list[x]
            i = x - 1
            
            while (i >= 0 and unsorted_list[i] > key):
                sorter.highlight(canvas, unsorted_list, i, True) 
                unsorted_list[i + 1] = unsorted_list[i]
                
                sorter.swap(canvas, unsorted_list, i, i+1)
                time.sleep(0.01)
                sorter.highlight(canvas, unsorted_list, i, False)
                i = i - 1
                
            unsorted_list[i + 1] = key
            
        
class SelectionSort():
    '''
    The class responsible for the implementation of the SelectionSort algorithm.
    Operates in n squared time worst-case
    '''
    
    def __init__(self: object, canvas: Canvas) -> None:
        unsorted_list = create_random_list()
        sorter = SortingGraphics(canvas, unsorted_list)\
            
        #start a thread of SelectionSort
        t = Thread(target = self.selection_sort, args = (sorter, canvas, unsorted_list))
        t.start()
        
    def selection_sort(self: object, sorter: SortingGraphics, canvas: Canvas, unsorted_list: list) -> None:
        '''
        Perform SelectionSort and call the graphics_interface functions to display.
        
        Algorithm: 
        - First find the smallest element in the array.
        - Exchange the smallest element with the element at the first position.
        - Repeat for n+1, n+2,...,n+x elements, until array is sorted.
        
        '''
        
        for x in range(0, len(unsorted_list)):
            index = x
            for y in range(x,len(unsorted_list)):
            #individual bars of interest are highlighted then turned back to normal
                sorter.highlight(canvas, unsorted_list, y, True)
                time.sleep(0.0005)
                if unsorted_list[index] > unsorted_list[y]:
                    index = y
                sorter.highlight(canvas, unsorted_list, y, False)
                     
            #swapping process
            unsorted_list[x], unsorted_list[index] = unsorted_list[index], unsorted_list[x] 
            sorter.swap(canvas, unsorted_list, x, index)
            
               
class BubbleSort():
    '''
    The class responsible for the implementation of the BubbleSort algorithm.
    TODO: operation time
    '''
    
    def __init__(self: object, canvas: Canvas) -> None:
        '''
        Will create an unsorted list which will undergo BubbleSort.
        '''
        unsorted_list = create_random_list()
        sorter = SortingGraphics(canvas, unsorted_list)
        
        #start a new thread of BubbleSort                         
        t = Thread(target = self.bubble_sort, args = (canvas, sorter, unsorted_list))
        t.start()
        
    def swap(self: object, canvas: Canvas, unordered_list: list, sorter: SortingGraphics, x: int, y: int ):
        '''
        Swap the necessary value.
        '''
        tmp = unordered_list[x]
        unordered_list[x] = unordered_list[y]
        unordered_list[y] = tmp      
        
        time.sleep(0.0005)
        sorter.swap(canvas, unordered_list, x, y)
        
                    
    def bubble_sort(self: object, canvas: Canvas, sorter: SortingGraphics, unordered_list: list) -> None:
        '''
        Perform BubbleSort and call the graphics_interface functions to display.
        '''
        for i in range(len(unordered_list)):
            for k in range(len(unordered_list) - 1, i, -1 ):
                if (unordered_list[k] < unordered_list[k - 1] ):
                    self.swap(canvas, unordered_list, sorter, k, k - 1)
        
    
class MergeSort():
    '''
    The class responsible for the implementation of the MergeSort algorithm.
    Operates in n(log n) time.
    '''
    
    def __init__(self: object, canvas: Canvas) -> None:
        
        #import information stored inside class attributes
        unsorted_list = create_random_list()
        self.sorter = SortingGraphics(canvas, unsorted_list)
        self.canvas = canvas
        
        self.merge_sort(unsorted_list)
        
        #start a new thread of MergeSort                         
        #t = Thread(target = self.merge_sort, arg = unsorted_list)
        #t.start()    
        
    def merge(self, left, right):
        result = []
        i ,j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result += left[i:]
        result += right[j:]
        
        return result
    
    def merge_sort(self, unsorted_list):
        '''
        Perform a MergeSort and call the graphics_interface functionality.
        '''
        if len(unsorted_list) < 2:
            return unsorted_list
        middle = len(unsorted_list) // 2
        left = self.merge_sort(unsorted_list[:middle])
        right = self.merge_sort(unsorted_list[middle:])
        return self.merge(left, right)          
    
class HeapSort():
    '''
    The class responsible for the implementation of the HeapSort algorithm.
    '''
    def __init__(self: object, canvas: Canvas) -> None:
        unsorted_list = create_random_list()
        sorter = SortingGraphics(canvas, unsorted_list)
        
        #starts a running thread
        t = Thread(target = self.heap_sort, args = (canvas, sorter, unsorted_list))
        t.start()
        
    def heapify(self: object, canvas: Canvas, sorter: SortingGraphics, unordered_list: list, end: int, i: int) -> None:
        '''
        Transform into Heap Order
        '''
        left = 2 * i + 1
        right = 2 * (i + 1)
        
        maximum = i
        if (left < end and unordered_list[i] < unordered_list[left]):
            maximum = left
        if (right < end and unordered_list[maximum] < unordered_list[right]):
            maximum = right
        if (maximum != i):
            self.swap(canvas, sorter, unordered_list, i, maximum)
            self.heapify(canvas, sorter, unordered_list, end, maximum)
            
    def swap(self: object, canvas: Canvas, sorter: SortingGraphics, unordered_list: list, i: int, j: int) -> None:
        '''
        Swap two values and update graphics.
        
        '''
        unordered_list[i], unordered_list[j] = unordered_list[j], unordered_list[i]
        sorter.swap(canvas, unordered_list, i, j)
        
        #create a delay
        time.sleep(0.005)
        
    def heap_sort(self: object, canvas: Canvas, sorter: SortingGraphics, unordered_list: list) -> None:
        '''
        Perform HeapSort and call the graphics_interface to display.
        '''
        end = len(unordered_list)
        start = end // ( 2 - 1)
        for i in range (start , -1, -1):
            self.heapify(canvas, sorter, unordered_list, end, i)
        for i in range(end - 1, 0, -1):
            self.swap(canvas, sorter, unordered_list, i, 0)
            self.heapify(canvas, sorter, unordered_list, i, 0)
    
    
class Dijkstra():
    '''
    The class responsible for the implementatino of Dijkstra's Shortest Path algorithm. 
    '''
    
    def dijkstra(graph, node):
        """
        Simulate the dijkstra algorithm in a graph
        """
        distance_to = {}
        distance_to[node] = 0
        distance_path = {}
        while (distance_to):
            #in case we have a disjoint graph
            op_node = min_distance(distance_to)
            distance_path[op_node] = distance_to[op_node]
            del distance_to[op_node]
            for x, x_len in graph[op_node].items():
                if x not in distance_path:
                    if x not in distance_to:
                        distance_to[x] = distance_path[op_node] + x_len
                    elif distance_to[x] > distance_path[op_node] + x_len:
                        distance_to[x] = distance_path[op_node] + x_len
        return distance_path    