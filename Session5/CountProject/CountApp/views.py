from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    text_without_blank = text.replace(" ", "")
    total_len = len(text)
    total_len_without_blank = len(text_without_blank)
    word = text.split(" ")
    word_len = len(word)
    return render(request, 'result.html', {'text' : text, 'total_len' : total_len,'total_len_without_blank' : total_len_without_blank, 'word_len' : word_len})
