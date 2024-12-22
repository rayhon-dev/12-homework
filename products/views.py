from django.shortcuts import render,redirect,get_object_or_404
from .models import Product


def home(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products }
    return render(request, 'products/product-list.html', ctx)



def product_create(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        price = request.POST.get('price')
        product_image = request.FILES.get('product_image')
        product_category = request.POST.get('product_category')

        if product_name and product_description and price and product_image and product_category:
            Product.objects.create(
                product_name=product_name,
                product_description=product_description,
                price=price,
                product_image=product_image,
                product_category=product_category
            )
            return redirect('products:list')

    return render(request, 'products/product-create.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product }
    return render(request, 'products/product-detail.html', ctx)

def about(request):
    return render(request, 'products/about.html')


