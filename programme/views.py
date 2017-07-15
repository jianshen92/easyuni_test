from django.shortcuts import render

# Create your views here.
def display_view(request):
    template_name = 'programme/display_view.html'

    return render(request, template_name)