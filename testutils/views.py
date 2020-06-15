from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request,'index.html')

def analyze(request):
     djtext = request.GET.get("text",'default')
     removepunc=request.GET.get("removepunc",'off')
     capfirst= request.GET.get("capfirst", 'off')
     newlinerremove= request.GET.get("newlinerremove", 'off')
     extraspaceremover= request.GET.get("extraspaceremover", 'off')

     if removepunc == "on":
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed = ""
          for char in djtext:
               if char not in punctuations:
                    analyzed = analyzed + char
          params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
          djtext=analyzed

     if newlinerremove=="on":
          analyzed = ""
          for char in djtext:
               if char !="\n" and char !="\r":
                    analyzed = analyzed + char
          params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}

     if extraspaceremover=="on":
          analyzed = ""
          for index,char in enumerate(djtext):
               if not(djtext[index]=="" and djtext[index+1]==""):
                    analyzed = analyzed + char
          params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
          djtext = analyzed

     if capfirst == "on":
          analyzed = ""
          for char in djtext:
               analyzed = analyzed + char.upper()
          params = {'purpose': 'UPPER CASE', 'analyzed_text': analyzed}
          djtext = analyzed

     if capfirst != "on" and extraspaceremover !="on"and newlinerremove !="on" and removepunc != "on":
          return HttpResponse("Error")

     return render(request,'analyze.html',params)
