import math
class Vector(object):
    
    """ A vector class for real numbers"""
    def  __init__(self, length, vector = None):
        self.length = length;
        self.vector = vector;

        if vector == None:
            vector = [0 for x in range(length)];
            self.vector = vector;
        
    def __str__(self):
       #print(self.vector);
        return str(self.vector);
    
    def __getitem__(self, index):
        return self.vector[index];
    
    def __setitem__(self,idx,item):
        self.vector[idx] = item;
        
    def __add__(self, v2):
        c = Vector(self.length)
        if (self.length == v2.length):
            for i in range (self.length):
                c[i] = self[i] + v2[i]
            return c;
        else:
            #If they have conflicting lengths 
            raise TypeError(); 
        
        
    def __mul__(self, x):
        a =self;
        
        if (isinstance(x, Vector)):
            #make sure they are the same length
            if (x.length == a.length ):
                sum = 0;
                for i in range(x.length):
                   sum = sum +  (x[i] * a[i])
                
                #This is a dot product so return the sum
                return sum;   
            
            else:
                raise TypeError();
            
        elif ( isinstance(x, int) or isinstance(x,float)):
             v_mul = Vector(a.length)
             for i in range(a.length):
                 v_mul[i] = a[i] * x
           
             return v_mul;
        
    def __rmul__(self,x):

        if (isinstance(x,int) or isinstance(x, float)):
            v_rmul = Vector(self.length);
            for i in range(self.length):
                v_rmul[i] = self[i] * x
            
            return v_rmul;
        
        
        elif(isinstance(x,Vector)):
            #Don't care, don't want it get the else though
            print ("Ignoring instance")
            pass
        else:
            print ("Wrong not a number or vector")
            raise TypeError();
    
    def magnitude(self):
        sum = 0;
        for i in self.vector:
            sum += i*i;
        return sum ** (.5)
    
    def half_magnitude(self):
        sum = 0; 
        for i in self.vector:
            sum += i*i;
        return sum;
    
    def __rshift__(self, v2):
        """ project vector self onto vector B proj b self """
        a = self
        if (isinstance(v2,Vector)):
            return (  (a*v2)*(v2.half_magnitude())**-1  )  * v2
            #return  ( (self*v2)/v2.magnitude() ) * v2
        
        
        else:
            raise  TypeError();
    
        
        
        
        
        

      
def Test():
    #A couple of starting tests
    a = Vector(4, [1,1,1,0]);
    b = Vector(4, [1,1,-1,-1]);
    #assert a.magnitude() == 3**.5;
    # assert a.half_magnitude() == 3; 
    print a
    print (a>>b)
    print a

    
    
    

    
   
