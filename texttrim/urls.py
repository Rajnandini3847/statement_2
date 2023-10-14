# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('nltk/', nltk, name='nltk'),
    path('gpt2/', gpt2, name='gpt2'),
    path('bert/', bert, name='bert'),
    path('xlnet/', xlnet, name='xlnet'),
    path('question/', questions, name='questions'),
    path('quiz/', quiz, name='quiz'),
    path('queries/', queries, name='queries'),
    path('upload/', upload_audio, name='upload'),
    path('translator_hin/',translator_hin,name='translator_hin')
]
