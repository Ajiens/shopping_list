from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Alwan Takahashi Aditama',
        'class': 'PBP E',
        'Hobskuy': 'Maen'
    }

    return render(request, "main.html", context)
