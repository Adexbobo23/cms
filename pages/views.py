from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def ticket(request):
    return render(request, 'ticket.html')


def faq(request):
    return render(request, 'faq.html')


def contact(request):
    return render(request, 'contact.html')