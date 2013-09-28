from tkinter import *
from tkinter import ttk
import time

class SortingGraphics():
    '''
    A class which is meant to be used as the graphical interface for sorting algorithms. Bars of various height are used for the different indexes and values of an unsorted list. 
    '''    
    
    def __init__(self: object, canvas: Canvas, array: list) -> None:
        '''
        Creates the original arrangement of bars for the unsorted list.
        '''
        
        #clear entire previous canvas
        canvas.delete('all')
        count = 0 #will be used to keep track of rectangle x
        #used to keep track of rectangle positions
        self.rectangle = []
        
        for value in array:
            x_top = count * 16 #800 width / 50 bars = 16 width per bar
            y_top = 600 - (value * 10)
            x_bottom = (count + 1) * 16
            y_bottom = 600
            count += 1
            
            self.rectangle.append((x_top, y_top, x_bottom, y_bottom))    
            canvas.create_rectangle(x_top, y_top, x_bottom, y_bottom, fill = 'blue')
        
        #must always remember to return to previous stack
        return
        
    def highlight(self: object, canvas: Canvas, array: list, index: int, current: bool) -> None:
        '''
        Highlights the specific bar of interest.
        '''
        (x_top, y_top, x_bottom, y_bottom) = self.rectangle[index]
        
        #current determines whether bar is current one being checked
        if (current):
            canvas.create_rectangle(x_top, y_top, x_bottom, y_bottom, fill = 'red')
        else:
            canvas.create_rectangle(x_top, y_top, x_bottom, y_bottom, fill = 'blue')

    def swap(self: object, canvas: Canvas, array: list, index_one: int, index_two: int) -> None:
        '''
        Will swap bars from two given positions. 
        '''
        
        #swap the self.rectangle tuple values for maintain rectangle coordinates
        (x_top, y_top, x_bottom, y_bottom) = self.rectangle[index_one]
        (x2_top, y2_top, x2_bottom, y2_bottom) = self.rectangle[index_two]
        self.rectangle[index_one] = ((x_top, y2_top, x_bottom, y2_bottom))
        self.rectangle[index_two] = ((x2_top, y_top, x2_bottom, y_bottom))
        
        #index_one bar changed
        canvas.create_rectangle(x_top, 0, x_bottom, y_bottom, fill = 'white', width = 0)
        canvas.create_rectangle(x_top, y2_top, x_bottom, y2_bottom, fill = 'blue')
        
        #index_two bar changed
        canvas.create_rectangle(x2_top, 0, x2_bottom, y2_bottom, fill = 'white', width = 0)
        canvas.create_rectangle(x2_top, y_top, x2_bottom, y_bottom, fill = 'blue')
        
        
        
        
        
        
        
        