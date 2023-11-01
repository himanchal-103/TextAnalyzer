# Manually created file
from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse('Home Page')
    return render(request, 'index.html')


def analyze(request):
    # Retrieving text input
    original_text = request.POST.get('text', 'default')
    djtext = original_text

    # Retrieving checkbox value (default value is off)
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off') 
    newlineremover = request.POST.get('newlineremover', 'off') 
    extraspaceremover = request.POST.get('extraspaceremover', 'off') 
    charcount = request.POST.get('charcount', 'off') 

    # Creating list of the parameters that are selected
    value = []
    if removepunc == 'on':
        value.append('Removed punctuations')
    if fullcaps == 'on':
        value.append('Changed to uppercase')
    if newlineremover == 'on':
        value.append('Removed new line')
    if extraspaceremover == 'on':
        value.append('Removed extra spaces')
    if charcount == 'on':
        value.append('Character Counter')

    # Check which check box is on and perform the task accordingly
    if value != []:
        if removepunc == 'on':
            punctuation_list = """=`+!()-[]{};:'"\,<>./?@#$%^&*_~"""
            analyzed = ""
            for char in djtext:
                if char not in punctuation_list:
                    analyzed += char
            djtext = analyzed

        if fullcaps == 'on':
            analyzed = ""
            for char in djtext:
                analyzed += char.upper()
            djtext = analyzed

        if newlineremover == 'on':
            analyzed=""
            for char in djtext:
                if char != '\n' and char != '\r':
                    analyzed += char
            djtext = analyzed

        if extraspaceremover == 'on':
            analyzed=""
            for index, char in enumerate(djtext):
                if char != " ":
                    analyzed += char
                elif djtext[index] == " " and djtext[index+1] != " ":
                    analyzed += djtext[index]
            djtext = analyzed

        if charcount == 'on':
            count = 0
            for char in djtext:
                if char != " " or char !='\n' or char !='\r':
                    count+=1
            djtext = djtext + '\n\nNumber of characters : ' + str(count)

        params = {'original' : original_text, 'purpose' : value, 'analyzed_text' : djtext}
        return render(request, 'analyze.html', params)
        
    else:
        return HttpResponse('ERROR : You did not selected any parameters')
