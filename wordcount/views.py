from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{ 'var' : 'HI there '})
def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    count = len(words)
    wordcount = dict()
    for w in words:
        if w in wordcount:
            wordcount[w] += 1
        else:
            wordcount[w] = 1
    sortedcount = sorted(wordcount.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{ 'fulltext' : fulltext , 'counts' : count ,'sortedcount' : sortedcount})
def about(request):
    return render(request,'about.html')
