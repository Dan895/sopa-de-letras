from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Create your views here.


def home(request):
    return render(request, 'sopaletras/home.html')


def about(request):
    return render(request, 'sopaletras/about.html')


def GenerarSopa(request):
    if request.method == 'POST':
        palabras = request.POST.getlist('palabras')
        # Procesa las palabras para generar la sopa
        # Coloca en mayusculas
        palabras = str(palabras).upper()

        letras = "abcdefghijklmnopqrstuvwxyz"

        # Genera el PDF
        response = HttpResponse(content='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sopa_letras.pdf"'

        # Generar PDF con ReportLab
        p = canvas.Canvas(response, pagesize=letter)
        # Agrega la sopa de letras al PDF
        p.drawString(100, 100, "Aqui va la sopa")
        p.showPage()
        p.save()

        # genera el pdf con la siguiente linea
        return response
