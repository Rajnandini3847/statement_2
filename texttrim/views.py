from django.shortcuts import render
from nltk import sent_tokenize
from .QNA.questions_gen import QuestionGenerator 
from .QNA.mcq_gen import QuizGenerator
from .MLFunctions.ask_queries import answer_question
from .MLFunctions.translator import translate_hindi_to_english

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
    model = 'NLTK'
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = main(text,lines)
        
        return render(request, 'results.html', {'summary': summary})
    return render(request, 'summary.html',{'model':model})

def gpt2(request):
    model = 'GPT2'
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = gpt2_summary(text,lines)
        return render(request, 'results.html', {'summary': summary})
    return render(request, 'summary.html',{'model':model})

def bert(request):
    model = 'BERT'
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = bert_summary(text,lines)
        return render(request, 'results.html', {'summary': summary})
    return render(request, 'summary.html',{'model':model})

def xlnet(request):
    model = 'XLNet'
    if request.method == 'POST':
        text = request.POST.get('text')
        lines = request.POST.get('lines')
        summary = xlnet_summary(text,lines)
        return render(request, 'results.html', {'summary': summary})
    return render(request, 'summary.html',{'model':model})



def questions(request):
    summary = request.POST.get('summary')

    if request.method == 'POST' and summary:
        sentences = sent_tokenize(summary)
        text = ' '.join(sentences)

        question_generator = QuestionGenerator(text)
        all_questions = question_generator.generate_all_questions()

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


def queries(request):
    if request.method == 'POST':
        context = request.POST.get('context', '')
        question = request.POST.get('question', '')
        answer = answer_question(context, question)
        return render(request, 'queries.html', {'context': context, 'question': question, 'answer': answer})

    return render(request, 'queries.html', {'context': '', 'question': '', 'answer': ''})


# views.py

from django.shortcuts import render, redirect
from .forms import AudioFileForm
from .models import AudioFile
from pydub import AudioSegment
from .MLFunctions.whisper_ai_v import transcribe_mp3
def process_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    processed_audio = audio.export(file_path.replace('.wav', '.mp3'), format='mp3')
    return processed_audio

def upload_audio(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save()
            file_path = audio_file.audio.path
            processed_audio = process_audio(file_path)
            audio_file.audio.name = audio_file.audio.name.replace('.wav', '.mp3')
            audio_file.audio.save(audio_file.audio.name, processed_audio)
            result = transcribe_mp3(file_path.replace('.wav', '.mp3'))
            
            return render(request, 'sucess.html', {'result': result})
    else:
        form = AudioFileForm()
    return render(request, 'upload_audio.html', {'form': form})

def translator_hin(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        summary = translate_hindi_to_english(text)
        return render(request, 'translator.html',{'summary':summary})
    return render(request, 'translator.html')