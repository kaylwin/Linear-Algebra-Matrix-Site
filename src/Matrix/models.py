from django.db import models

# Create your models here.
class Matrix(models.Model):
    #Number of rows 
    m =  models.IntegerField(default=0)
    #Number of Columns 
    n =  models.IntegerField(default=0)
    
    
    #need to use lists to work with the matrix
    
    
    def __str__(self):
        return "New matrix class"
    
    
    #Make it go through unless specified otherwise 
    def __init__(self, init = True):
        n =self.n
        m = self.m
        

        # initialize matrix [[0,0,0,0],[0,0,0,0]... etc.
        rows = [[0]*n for x in (m)] 
        # need to overload methods 
        
        
        
        
        
        
        
        
        #What to do here 
        
    
    
    