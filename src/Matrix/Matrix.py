
import math
from Vector import *
class Matrix(object):
    """ A m x n mtx of real numbers"""
    # This will be the mtx holding the data
    # Round No is accuracy
    def __init__(self, m , n, mtx=None, round_no=3):
        # rows 
        self.m = m;
        self.n = n;
        self.round_no = round_no;
        if mtx == None:
            # Initialize the mtx
            
            
            # TODO set this to be a list of vectors
            mtx = [Vector(n) for x in range (m)];
            
            self.mtx = mtx;  
            
        else: 
            temp_matrix = [];
            temp_mtx_col_len = len(mtx[0])
            for i in range(len(mtx)):
                temp_matrix.append(Vector(temp_mtx_col_len, mtx[i]));
            self.mtx = temp_matrix;
        
        
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
    
    def toList(self):
        list = [];
        for i in range(self.m):
            list.append(self[i].vector); 
        return list
                  
    def __getitem__(self, idx):
        """ Returns an item at mtx[][]"""
        # return the M[][] at the requested index
        return  self.mtx[idx]
        
    def resize(self, rows, cols):
        """ Resize the mtx"""
        # Erase the mtx and resize it 
        self.m = rows; 
        self.n = cols;
        M = [[0] * cols for x in rows]
        self.mtx = M
        return True
    
    def __setitem__(self, idx, item):
        
         self.mtx[idx] = item;
            
            
    def __add__(self, x):
        a = self
        b = x 
       
        if(a.m == b.m  and a.n == b.n):
             c = Matrix(a.m, a, n);
             for i in range(a.m):
                for j in range(a.n):
                    c[i][j] = b[i][j] + a[i][j]
                
        return c
    
    def __str__(self):
        """ Return the mtx"""
        mtxPrint = ""
        m = self.m 
        n = self.n 
        M = self.mtx
        
        for i in range(m):
            mtxPrint += "\n"
            for j in range(n):
                # round because no one wants to see the bzillionth digit
                mtxPrint += " " + str(round(M[i][j], 3) + 0.00) + " ";
               
        return mtxPrint
               
    def __mul__(self, x):
        # need to test to see if it's int or another matrix
        
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
                        for x in range(va.length):
                            product.append(va[x] * vb[x])
                            dot = 0;
                            for item in product:
                                dot += item
                                c[i][j] = dot
                return c
        
        
        elif (isinstance(x, int)):
            # Multiply Everything in the matrix 
            c = Matrix(self.m, self.n);
            for i in range(self.m):
                for j in range(self.n):
                    c[i][j] = self[i][j] * x
            return c
               
    def __rmul__(self, x):
   
        # Matrix multiplication is one sided so not including
        # conflicting matrix 
        if (isinstance(x, int)):
            # Multiply Everything in the matrix 
            c = Matrix(self.m, self.n)
            for i in range(self.m):
                for j in range(self.n):
                    c[i][j] = self[i][j] * x
            return c    
            
    def __invert__(self):
        
        
        
        c = Matrix(self.m, self.n * 2);
        
        for i in range(c.m):
            for j in range(c.n):
                if(j < self.m):
                    c[i][j] = self[i][j];
                if(j >= self.n and i + self.n == j):
                    c[i][j] = 1;
        c = c.rref();
        d = Matrix(self.m, self.n);
        for i in range(c.m):
            for j in range(c.n):
                if(j >= self.n):
                    d[i][j - (self.n)] = c[i][j]
        return d
        
        
    def Transpose(self):
        c = self
        d = Matrix(c.n, c.m)
        for i in range(c.n):
            for j in range(c.m):
                d[i][j] = c[j][i]
        return d
          
    def getColumn(self, idx):
        a = self
        c = Vector(self[0].length);
        for i in range(a.m):
            for j in range(a.n):
                if j == idx:
                   c[i] = a[i][j]
        return c

    def rref(self):
        d = self
        refmtx = Matrix(d.m, d.n, d.toList())
        columnRestriction = None
        # Set ColumnRestriction = to whichever is less
        if refmtx.m > refmtx.n: 
            columnRestriction = refmtx.n;
        else: 
            columnRestriction = refmtx.m;
        

        zeroSwitcher = 0
        while refmtx[0][0] == 0:
           
            zeroSwitcher += 1 
            row1 = refmtx[0]
            row2 = refmtx[zeroSwitcher]
            
            for k in range(row2.length):
                # set the first row = to row2
                refmtx[0][k] = row2[k]
                # set teh second row = row1
                refmtx[zeroSwitcher][k] = row1[k]
                
            if zeroSwitcher == refmtx.m:
                print ("Matrix reduce failed :(")
        
      
        for j in range(columnRestriction - 1):
            skip = False;
            for i in range((refmtx.m - j - 1)):
             
                # Make sure the header of a column is not 0 
                if (refmtx[j][j]) != 0:
                    skip = False;
            
                else:
                    
                    counter = 0
                    while (refmtx[j][j] == 0) :
                        # J is the current column
                        # counter is the current row
                        counter += 1 
                        # row c is the first row
                        rowC = refmtx[j]
                        # counter is the row we are looking for 
                        rowJ = refmtx[counter]
                        
                        for k in range(rowC.length):
                            # set teh first row = to row2
                            refmtx[j][k] = rowJ[k]
                            
                            # set the second row = to row1 
                            refmtx[counter][k] = rowC[k]
                            
                            
                        # if everything = 0 then jsut screw it and don't do anything
                        
                        # TODO 
                        if counter == (refmtx.m - 1) and refmtx[j][j] == 0:
                            
                            skip = True;
                            break
           
                if skip == False:
                    
                    if(refmtx[i + j + 1][j] != 0):
                       
                        # get the scalar from the first row to multiply by
                        rowScalar = refmtx[i + j + 1][j] * ((refmtx[j][j]) ** -1)
                        
                        Rj = rowScalar * refmtx[j]  # [x*rowScalar for x in c[j]]
                        Ri = refmtx[i + 1 + j]

                        refmtx[i + 1 + j] = Ri + -1 * Rj
                       # resultantRow = [Ri[x] - Rj[x] for x in range(Rj.length)]
                        
                        # Read the items back into the matrix 
                        
                        
                            
        # Reducing the upper part now 
        print (refmtx)
        for j in range(columnRestriction - 1):
            for i in range(refmtx.m - (1 + j)):
                skip = False;
                
                # print ("bottomRow", [c.m-j-1], [c.n-1-j-(c.n-columnRestriction)])
                
                bottomRow = refmtx[(refmtx.m - j - 1)][(refmtx.n - 1 - j - (refmtx.n - columnRestriction))]
                
                upperRow = refmtx[refmtx.m - 2 - i - j][(refmtx.n - 1 - j - (refmtx.n - columnRestriction))]
                # print ("UpperRow", [c.m-2-i-j], [c.n-1-j-(c.n-columnRestriction)])
                
                
                # Make it so that it won't divide with a 0
                if upperRow == 0 or bottomRow == 0:
                    skip = True
                if (skip == False):
                    rowScalar = bottomRow / upperRow;
                    row1 = refmtx[refmtx.m - j - 1]
                    
                    
                    # changed this 
                    # row2 = [x*rowScalar for x in c[c.m-2-i-j] ]
                    row2 = rowScalar * refmtx[refmtx.m - 2 - i - j];
                    # resultantRow = [row1[z] - row2[z] for z in range(row1.length)]
                    refmtx[refmtx.m - (2 + i + j)] = row1 + -1 * row2
                    # Read out the results back into the matrx 
                    # for k in range(len(resultantRow)):
                      #  c[c.m-(2+i+j)][k] = resultantRow[k]
        
        print (refmtx)
        
        for i in range(refmtx.m):
            for j in range(refmtx.n):
                if (i == j):
                    if (refmtx[i][j] != 0):
                        scalar = refmtx[i][j] ** -1
                        refmtx[i] = refmtx[i] * scalar
                        
                
        print(refmtx)              
        z = refmtx
        return refmtx
        
    def orthagonalize(self):
        E = Matrix(self.m, self.n);
        
        
        E[0] = self[0];

        for column in range (1, self.m):
            
            sum = Vector(self.n)
            # May want to have it start at 1 instead of zero
           
            for position in range(column):
                sum = sum + (self[column] >> E[position]);
                

            sum = sum * -1
            sum = sum + self[column]
            E[column] = sum;
            

        
        return E
            
    def getEigens(self):
        if self.m != self.n:
            raise TypeError;
        # self = self.Transpose();
        run = True;
      
        mtx = self;
        count = 0;
        while(run):
            A = mtx.Transpose();
            F = A.orthagonalize();
            Q = Matrix(A.m, A.n)
            for i in range(A.m):
                Q[i] = (((F[i].magnitude()) ** -1) * F[i]);

            R = Matrix(A.m, A.n);
        
            for i in range (A.m):
                for j in range(A.n):
                    if i == j:
                        R[i][j] = F[i].magnitude();
                    elif i > j:
                            R[i][j] = 0;
                
                    elif i < j:
                        R[i][j] = A[j] * Q[i];
          
            count += 1;
            
            # mtx.m, mtx.n 
           # print (R*Q)
           
            if (count > 20):
                
                new_sum = 0;
                old_sum = 0;
                mtx_new = R * Q;
                
                for i in range(mtx.m):
                    for j in range(mtx.n):
                        if i == j:
                            new_sum += mtx_new[i][j]
                            old_sum += mtx[i][j]
                 
                if (abs(abs(old_sum) - abs(new_sum)) < .0001):
                    run = False;
            
            
                mtx = mtx_new;
                run = False;
            else:
          
                mtx = R * Q;
        
        
        
          
        output = []
        for i in range(mtx.m):
            for j in range(mtx.n):
                if i == j:
                    # Change to get more accurate numbers
                    output.append(round(mtx[i][j], mtx.round_no))
        return output
                    
                    
                    
    
        
        
        
  
    
def test():
    a = Matrix(2, 1, [[1], [1]])
    b = Matrix(2, 2, [[0, 1], [-1, 0]])
    
    assert(a * b == None);
    
   
    # Orthagonality Tests 
    a = Matrix(3, 3, [[3, 2, 1], [6, 5, 2], [1, 5, 2]]);
    b = Matrix(2, 2, [[1, 1], [2, 0]])
    # a = Matrix(2,2, [[1.4,1.8], [.8, -.4]])
    # assert a.orthagoalize() == Matrix(3,4,[[1,1,-1,-1], [2,1,1,2],[0.4, -0.3, 0.7, -0.6]])
   

   # print (a)
   # print (a.orthagonalize())
   # print (a.rref());
    # print (a.rref())
   # print (a.rref(), "\n\n")
    print(a)
    print (a.getEigens());
    print (b.getEigens())
    # print (~a)
    # print (a.getEigens())
test();


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
