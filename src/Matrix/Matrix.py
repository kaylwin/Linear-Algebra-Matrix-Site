
import operator
import inspect 
class Matrix(object):
    """ A m x n mtx of real numbers"""
    # This will be the mtx holding the data

    def __init__(self, m , n, mtx = None):
        # rows 
        self.m = m;
        self.n = n;
        self.mtx = mtx 
        if mtx == None:
            # Initialize the mtx
            mtx = [[0] * n for x in range (m)];
            self.mtx = mtx;  
           
        
    def __eq__ (self, x):
        """Check to see if two matrices are equal"""
        mtx = self.mtx
        m = self.m
        n = self.n 
        
        m1 = x.m
        n1 = x.n
        
        if m1 != m or n != n1:
            return False
        
        for i in range(m):
            for j in range(n):
                # Compare each item to see if anything is different
                if x[i][j] != mtx[i][j]:
                    return False;
                    
        return True
                
    def __getitem__(self, idx):
        """ Returns an item at mtx[][]"""
        # return the M[][] at the requested index
        return self.mtx[idx]
        
    def resize(self, rows, cols):
        """ Resize the mtx"""
        # Erase the mtx and resize it 
        self.m = rows; 
        self.n = cols;
        M = [[0] * cols for x in rows]
        self.mtx = M
        return True
    
    
   
    def __setitem__(self,idx,item):
        if len(self.mtx[idx]) == len(item):
            self.mtx[idx] = item;
        else: 
            raise "Incorrect Dimension"
            
    def __add__(self,x):
        a = self
        b = x 
        if( a.m == b.m  and a.n == b.n):
            for i in range(a.m):
                for j in range(a.n):
                    a[i][j] = b[i][j] + a[i][j]
                
        return a
        
        
        
    def __str__(self):
        """ Return the mtx"""
        mtxPrint = ""
        m = self.m 
        n = self.n 
        M = self.mtx
        
        for i in range(m):
            mtxPrint += "\n"
            for j in range(n):
                mtxPrint += " " + str(M[i][j]) + " ";
               
        return mtxPrint
               


    def __mul__(self,x):
        #need to test to see if it's int or another matrix
        
        if (isinstance(x, Matrix)):
            a = self
            b = x 
            # x * a 
            c = Matrix(a.m, b.n)
            if a.n == b.m:
                for i in range(a.m):
                    for j in range(b.n):
                        va = a[i]
                        vb = b.getColumn(j)
                        product = []
                        for x in range(len(va)):
                            product.append(va[x] * vb[x])
                            dot = 0;
                            for item in product:
                                dot += item
                                c[i][j] = dot
                return c
        
        
        elif (isinstance(x,int)):
            #Multiply Everything in the matrix 
            a  = self 
            for i in range(a.m):
                for j in range(a.n):
                    a[i][j] = a[i][j] * x
            return a    
            
            
        
    def __rmul__(self,x):
        # reverse of the multipl
        """ Overrides the * operator to 
        reverse multiply matrices"""
        if (isinstance(x, Matrix)):
            a = self
            b = x 
            # x * a 
            c = Matrix(a.m, b.n)
            if a.n == b.m:
                for i in range(a.m):
                    for j in range(b.n):
                        va = a[i]
                        vb = b.getColumn(j)
                        product = []
                        for x in range(len(va)):
                            product.append(va[x] * vb[x])
                            dot = 0;
                            for item in product:
                                dot += item
                                c[i][j] = dot
                return c
            
        elif (isinstance(x,int)):
            #Multiply Everything in the matrix 
            a  = self 
            for i in range(a.m):
                for j in range(a.n):
                    a[i][j] = a[i][j] * x
            return a    
            
    
    def getColumn(self,idx):
        a= self
        c = []
        for i in range(a.m):
            for j in range(a.n):
                if j == idx:
                   c.append(a[i][j])
        return c

    
    
    
    def rref(self):
        c = self
        columnRestriction = None
        #Set ColumnRestriction = to whichever is less
        if c.m > c.n: 
            columnRestriction = c.n;
        else: 
            columnRestriction = c.m;
        

        zeroSwitcher = 0
        while c[0][0] == 0:
           
            zeroSwitcher += 1 
            row1 = c[0]
            row2 = c[zeroSwitcher]
            
            for k in range(len(row2)):
                #set the first row = to row2
                c[0][k] = row2[k]
                #set teh second row = row1
                c[zeroSwitcher][k] = row1[k]
                
            if zeroSwitcher == c.m:
                print ("Matrix reduce failed :(")
        
       
        for j in range(columnRestriction-1):
          
            skip = False;
            for i in range((c.m - j -1 )):
             
                #Make sure the header of a column is not 0 
                if (c[j][j]) != 0:
                    skip = False;
            
                else:
                    
                    counter = 0
                    while (c[j][j] == 0 ) :
                        #J is the current column
                        #counter is the current row
                        counter +=1 
                        #row c is the first row
                        rowC = c[j]
                        #counter is the row we are looking for 
                        rowJ = c[counter]
                        
                        for k in range(len(rowC)):
                            #set teh first row = to row2
                            c[j][k] = rowJ[k]
                            
                            # set the second row = to row1 
                            c[counter][k] = rowC[k]
                            
                            
                        #if everything = 0 then jsut screw it and don't do anything
                        if counter == (r.m-1) and c[j][j] == 0:
                            
                            skip = True;
                            break
                if skip == False:
                    
                    if(c[i+j+1][j] != 0 ):
                       
                        #get the scalar from the first row to multiply by
                        rowScalar = c[i+j+1][j]/(c[j][j])
                        
                        Rj = [x*rowScalar for x in c[j]]
                        Ri = c[i+1+j]

                        
                        resultantRow = [Ri[x] - Rj[x] for x in range(len(Rj))]
                        
                        #Read the items back into the matrix 
                        
                        for k in range(len(resultantRow)):
                            c[i+1+j][k] = resultantRow[k]
                            
        #Reducing the upper part now 
        
        for j in range(columnRestriction-1):
            for i in range(c.m - (1+j)):
                skip = False;
                
                bottomRow = c[(c.m-j-1)][(c.n-1-j-(c.n-columnRestriction))]
                upperRow =  c[c.m-(2+i+j)][(c.n-1-j-(c.n-columnRestriction))]
                
                #Make it so that it won't divide with a 0
                if upperRow == 0 or bottomRow == 0:
                    skip = True
                if (skip == False):
                    rowScalar = bottomRow/upperRow;
                    row1 = c[c.m-j-1]
                    row2 = [x*rowScalar for x in c[c.m-2+i+j] ]
                    resultantRow = [row1[z] - row2[z] for z in range(len(row1))]
                    
                    #Read out the results back into the matrx 
                    for k in range(len(resultantRow)):
                        c[c.m-(2+i+j)][k] = resultantRow[k]
                    
        for i in range (c.n):
            for j in range(c.m):
                if (i == j):
                    if (c[i][j] != 0):
                        scalar = 1/c[i][j]
                        outputRow = [x*scalar for x in c[i]]
                        for k in range(len(outputRow)):
                            c[i][k] = outputRow[k]
                            
        return c        
    
        
        
        
        
        
        
        
    
    
    
    
def test():
  
    a = Matrix(3,4,[[1,2,3,4],[5,1,2,4], [6,9,8,4]])
    print (a)
    
    print(a.rref())
    
    
    
    
if test():
    print ("Tests passed")
#Start Script 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
