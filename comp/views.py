from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.http import HttpResponse
from .utils import render_to_pdf
def index(request):
    return render(request,"index.html") 
def pdf(request):
    name="Anu"
    address="Mannarkkad"
    context = {
        "name":name,
        "address":address
    }
    template_name = "pdf.html"
    return render_to_pdf(template_name,context)
