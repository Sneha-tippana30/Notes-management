from django.shortcuts import render, redirect
from .models import Question


def home(request):
    all_notes = Question.objects.all()
    return render(request, 'home.html', {'notes': all_notes})


def addnote(request):
    if request.method == 'POST':
        category = request.POST['category']
        question = request.POST['question']
        answer = request.POST['answer']
        Question.objects.create(category=category,question=question,answer=answer)
        return redirect('home')
    return render(request, 'add.html')


def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == 'POST':
        question.category = request.POST['category']
        question.question = request.POST['question']
        question.answer = request.POST['answer']
        question.save()
        return redirect('home')
    return render(request, 'update.html', {'note': question})


def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('home')   

def python(request):
    python_notes = Question.objects.filter(category='Python')
    return render(request, 'python.html', {'notes': python_notes})
    
def django(request):
    django_notes = Question.objects.filter(category='Django')
    return render(request, 'django.html', {'notes': django_notes})

def sql(request):
    sql_notes = Question.objects.filter(category='SQL')
    return render(request, 'sql.html', {'notes': sql_notes})

def frontend(request):
    frontend_notes = Question.objects.filter(category='Frontend')
    return render(request, 'frontend.html', {'notes': frontend_notes})

def aiml(request):
    aiml_notes = Question.objects.filter(category='aiml')
    return render(request, 'aiml.html', {'notes': aiml_notes})
