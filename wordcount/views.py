from django.http import HttpResponse
from django.shortcuts import render
import operator

def egg(request):
    return HttpResponse('<h1>Eggs</h1>')

def home(request):
    return render(request,'home.html',{'hithere':'Sup bro'})

def count(request):
    fulltext=request.GET['fulltext']
    wordlist= fulltext.split();
    word_Dictionary = {}

    for word in wordlist:
        if word in word_Dictionary:
            word_Dictionary[word]+=1
        else:
            word_Dictionary[word]=1

    sortedwords= sorted(word_Dictionary.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count2':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'aboutus.html')
