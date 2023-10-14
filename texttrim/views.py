from django.shortcuts import render
from nltk import sent_tokenize
from .QNA.questions_gen import QuestionGenerator 
from .QNA.mcq_gen import QuizGenerator
# Create your views here.

def home(request):
    return render(request, 'index.html')

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .MLFunctions.nltk import main
from .MLFunctions.gpt2 import gpt2_summary
from .MLFunctions.bert import bert_summary
from .MLFunctions.xlnet import xlnet_summary

def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            error_message = 'Invalid username or password.'

    return render(request, 'login.html', {'error_message': error_message})

def signup_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
        elif User.objects.filter(email=email).exists():
            error_message = 'Email already exists. Please use a different one.'
        else:
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  

    return render(request, 'signup.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')  

def nltk(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = main(text,lines)
        return render(request, 'summary.html', {'summary': summary})
    return render(request, 'summary.html')

def gpt2(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = gpt2_summary(text,lines)
        return render(request, 'summary.html', {'summary': summary})
    return render(request, 'summary.html')

def bert(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = bert_summary(text,lines)
        return render(request, 'summary.html', {'summary': summary})
    return render(request, 'summary.html')

def xlnet(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = xlnet_summary(text,lines)
        return render(request, 'summary.html', {'summary': summary})
    return render(request, 'summary.html')



def questions(request):
    summary = request.POST.get('summary')

    if request.method == 'POST' and summary:
        sentences = sent_tokenize(summary)
        text = ' '.join(sentences)

        question_generator = QuestionGenerator(text)
        all_questions = question_generator.generate_all_questions()

        # Pass the questions and summary to the template
        return render(request, 'questions.html', {'summary': summary, 'all_questions': all_questions})
    
    return render(request, 'questions.html', {'summary': summary})


def quiz(request):
    summary = request.POST.get('summary')

    if request.method == 'POST' and summary:
        sentences = sent_tokenize(summary)
        text = ' '.join(sentences)

        quiz_generator = QuizGenerator(text)
        quiz_questions = quiz_generator.generate_all_questions()

        return render(request, 'quiz.html', {'summary': summary, 'quiz_questions': quiz_questions})
    
    return render(request, 'quiz.html', {'summary': summary})