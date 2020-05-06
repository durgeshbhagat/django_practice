
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    # return request object
    return render( request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    print('fulltext:{}'.format(fulltext))
    word_list = fulltext.split()
    word_count_dict = {}
    for word in word_list:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] +=1
    wordcount_list = list(word_count_dict.items())
    wordcount_list.sort(key = lambda item : item[-1], reverse=True)
    print(wordcount_list)
    return render(request, 'count.html', {'fulltext' : fulltext, 'count' : len(word_list), 'wordcount_list' : wordcount_list})


def aboutus(request):

    return render(request, 'aboutus.html', {})
