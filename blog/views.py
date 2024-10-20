from django.http import Http404
from django.shortcuts import render
from .models import Product,Carusel,Customer,About
# Create your views here.
def index(request):
    product = Product.objects.all()
    carousel = Carusel.objects.all()
    about = About.objects.all()
    customer = Customer.objects.all()


    context = {
        "product": product,
        "carousel": carousel,
        'about':about,
        'customer':customer
    }
    return render(request, 'index.html',context=context)
def about(request):
    about = About.objects.all()

    context = {
        'about': about,
    }
    return render(request, 'about.html',context=context)
def contact(request):
    return render(request, 'contact.html',context={})
def client(request):
    customer = Customer.objects.all()

    context ={
        'customer': customer
    }
    return render(request, 'client.html',context=context)

def products(request):
    product = Product.objects.all()
    context= {
        'pro': product
    }
    return render(request, 'products.html',context=context)

def productdetailView(request,id):
    try:
        blog = Product.objects.get(id=id)
        context = {
            'blog':blog
        }
    except blog.DoesNotExist:
        raise Http404("No blog found")
    return render(request, 'details/productDetail.html', context=context)


def aboutdetailView(request,id):
    try:
        blog = About.objects.get(id=id)
        context = {
            'blog':blog
        }
    except blog.DoesNotExist:
        raise Http404("No blog found")
    return render(request, 'details/aboutDetail.html', context=context)



def caruseldetailView(request,id):
    try:
        blog = Carusel.objects.get(id=id)
        context = {
            'blog': blog
        }
    except blog.DoesNotExist:
        raise Http404("No blog found")
    return render(request, 'details/caruselDetail.html', context=context)



def customerdetailView(request,id):
    try:
        blog = Customer.objects.get(id=id)
        context = {
            'blog': blog
        }
    except blog.DoesNotExist:
        raise Http404("No blog found")
    return render(request, 'details/customerDetail.html', context=context)




