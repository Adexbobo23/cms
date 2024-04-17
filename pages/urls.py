from django.urls import path
from .views import home, ticket, faq, contact

urlpatterns = [
    path('', home, name='home'),
    path('support-ticket/', ticket, name='ticket'),
    path('faq/', faq, name='faq'),
    path('contact/', contact, name='contact'),
]