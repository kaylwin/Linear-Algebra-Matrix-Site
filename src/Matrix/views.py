from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import json
from Matrix import *

# Create your views here.
class Home(TemplateView):
    template_name = "Matrix/matrix_operations.html"


class Entry(TemplateView):
    template_name = "Matrix/main.html"
    

        
def Orthagonalize(request):
    
    mtx= getMtx(request);
    mtx = mtx.orthagonalize();
    
    #Put it back into a stringified Matrix

    string_matrix = json.dumps(mtx.toList());
   
   
   #NEED TO FINISH
   #EXPORT as json, need to type in javscript class to revieve
    return HttpResponse(string_matrix);#str(string_matrix));
    

def getEigens(request):
    mtx = getMtx(request);
    print mtx
    eigens = mtx.getEigens();
    print eigens
    string_matrix = json.dumps(eigens);
    return HttpResponse(string_matrix);




def Invert(request):
    """Returns an inverted matrix from an AJAX request"""
    mtx = getMtx(request);
    mtx = ~mtx;
    for i in range(mtx.m):
        for j in range(mtx.n):
            mtx[i][j] = round(mtx[i][j],3)
    return HttpResponse(json.dumps(mtx.toList()));
    
def RREF(request):
    """Returns a reduced matrix from an AJAX request"""
    mtx = getMtx(request);
    mtx = mtx.rref();
    for i in range(mtx.m):
        for j in range(mtx.n):
            mtx[i][j] = round(mtx[i][j],3)
    return HttpResponse(json.dumps(mtx.toList()));
def getMtx(request):
    """Returns a matrix from a request"""
    string_matrix = request.GET['matrix_string'];
    matrix_list =  (json.loads(string_matrix))
    mtx = Matrix(len(matrix_list),len(matrix_list[0]), matrix_list);
    return mtx;
    
    
    
