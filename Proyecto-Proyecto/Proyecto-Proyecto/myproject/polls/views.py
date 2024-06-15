from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Escoge una opción por favor",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
import requests

def rickymorty(request):
    api_url = 'https://rickandmortyapi.com/api/character/5'
    response = requests.get(api_url)
    data = []
    if response.status_code == 200:
        data = response.json()
        print(data)
    return render(request, 'polls/testapirick.html', {'data': data})


def calculadora(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', ''))
        num2 = float(request.POST.get('num2', ''))
        operacion = request.POST.get('operacion', '')

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = 'Error: División por cero'
        else:
            resultado = 'Operación no válida'

        return render(request, 'polls/calculadora.html', {'resultado': resultado})

    return render(request, 'polls/calculadora.html')


def rickylista(request):
    if request.method == 'GET':
        personaje = request.GET.get('personaje', '')  
        if personaje:
            api_url = f'https://rickandmortyapi.com/api/character/{personaje}'
            response = requests.get(api_url)
            resultado = {}
            if response.status_code == 200:
                resultado = response.json()
            else:
                resultado = {'ERROR': 'Su personaje no existe :('}
            return render(request, 'polls/numrick.html', {'resultado': resultado})
        else:
            return render(request, 'polls/numrick.html', {'ERROR': 'Ingrese un número de personaje'})  
    return render(request, 'polls/numrick.html')

from .models import Cliente
def cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        sexo = request.POST.get("sexo")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")

        if not nombre or not edad or not sexo or not email or not telefono:
            return JsonResponse({'ERROR': 'Por favor, completa todos los campos'}, status=400)
        try:
            edad = int(edad)
            if edad < 18:
                return JsonResponse({'ERROR': 'Debes ser mayor de 18 años para registrarte'}, status=400)
        except ValueError:
            return JsonResponse({'ERROR': 'Edad no válida'}, status=400)

        if len(telefono) != 10:
            return JsonResponse({'ERROR': 'El número de teléfono debe tener 10 dígitos'}, status=400)

        cliente = Cliente(nombre=nombre, edad=edad, sexo=sexo, email=email, telefono=telefono)
        cliente.save()

        return JsonResponse({'Mensaje': 'Cliente guardado exitosamente'})

    return render(request, 'polls/Agendacliente.html')

from .models import Cliente

def lista_usuarios(request):
    usuarios = Cliente.objects.all()
    return render(request, 'polls/ListaUsuarios.html', {'usuarios': usuarios})

from .models import Usuario
def inicio (request):
    if request.method == 'POST':
        usuario = request.POST.get("usuario")
        contraseña = request.POST.get("contraseña")
    
        if not usuario or not contraseña:
            return render(request, 'polls/error.html', {'mensaje': 'Por favor, completa todos los campos'}, status=400)
        inicio = Usuario(usuario=usuario, contraseña=contraseña)
        inicio.save()

        return render(request, 'polls/exito.html')

    return render(request, 'polls/sesion.html')

def verinicios(request):
    ver = Usuario.objects.all()
    return render (request, 'polls/verinicio.html',{'ver':ver})





        


    
        







