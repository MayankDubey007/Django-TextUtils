# Views.py
# I have created this file - Mayank D
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    
    Pera = request.GET.get('Pera','default')
    Rpunc = request.GET.get('Rpunc','off')
    Upper = request.GET.get('Upper','off')
    Lower = request.GET.get('Lower','off')
    Capitalize = request.GET.get('Capitalize','off')
    Rnewline = request.GET.get('Rnewline','off')
    #REMOVE PUNTUATION
    Pera1 = Pera 
    if ((Rpunc == 'off') and (Upper == 'off') and (Lower == 'off') and (Capitalize == 'off') and (Rnewline == 'off')):
        params = {'PURPOSE':"You Did Not On Any Switch",'before':Pera1,'after':Pera}
        return render(request, 'analyze.html',params)
    if Rpunc == 'on':
        punc='''!@#$%^&*()_+{}|:"?></.,';\][]~'''
        result = ""
        for char in Pera:
            if char not in punc:
                result = result + char
        Pera = result
    #UPPERCASE
    if(Upper == 'on'):
        result = ""
        for char in Pera:
            result = result + char.upper()
        Pera = result
    #LOWERCASE 
    if(Lower == "on"):
        result = ""
        for char in Pera:
            result = result + char.lower()
        Pera = result
    #R-NEWLINE
    if(Rnewline=='on'):        
        result = ""
        for char in Pera:
            if char != "\n" and char !="\r":
                result = result + char
        Pera = result
    params = {'PURPOSE':"Remove NewLine",'before':Pera1,'after':result}
    return render(request, 'analyze.html',params)