from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'page1.html',{})

class Productlist(View):
    def get(self,request):
        produits=Product.objects.all()
        return render(request,'listProduct.html',{'prods':produits})



class Vehicule(View):
    def get(self,request):
        var1=Product.objects.filter(category='voiture')
        return render(request,'vehicule.html',{'context':var1})

class Immobilier(View):
    def get(self,request):
        var1 = Product.objects.filter(category='immobilier')
        return render(request,'immobilier.html',{'context':var1})

class Informatique(View):
    def get(self,request):
        var1 = Product.objects.filter(category='téléphone')
        return render(request,'informatique.html',{'context':var1})

class Loisir(View):
    def get(self,request):
        var1 = Product.objects.filter(category='loisirs')
        return render(request,'loisir.html',{'context':var1})

class ProductDetails(View):
    def get(self,request,id):
        product=Product.objects.get(id=id)
        return render(request,'detail.html',{'produit':product})
