from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def analyzer(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    NewLineRemover= request.POST.get('NewLineRemover','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcount','off')
    analyzed = ""
    # this remove punctuation from the text   
    if removepunc =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"Punctuation Remover" ,"analyzed_text":analyzed}
        # return render(request,'analyzer1.html',params)
        djtext = analyzed
    # convert text into upper case
    if fullcaps =='on':
        # analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose':"Converted to Uppercase" ,"analyzed_text":analyzed}
        # return render(request,'analyzer1.html',params)
        djtext = analyzed
    # Remove new line from the sentence
    if  NewLineRemover =='on':
        # analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r" :
                analyzed = analyzed + char
        params = {'purpose':"remove new line" ,"analyzed_text":analyzed}
        # return render(request,'analyzer1.html',params)
        djtext = analyzed
    # Remove extra space from the sentence
    if  extraspaceremover =='on':
        # analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':"extraspaceremover" ,"analyzed_text":analyzed}
        # return render(request,'analyzer1.html',params)
        djtext = analyzed

    # count char in the sentence
    if  charcounter =='on':
        count = 0
        for char in djtext:
            if char!=" ":
                count+=1
        params = {'purpose':"charcounter" ,"analyzed_text":f"total number of char in : {count}"}
    if(removepunc!="no" and NewLineRemover !='on' and fullcaps !='on' and extraspaceremover !='on' and  charcounter !='on'):
        return HttpResponse("Error")
    return render(request , 'analyzer.html' ,params)