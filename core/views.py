from django.shortcuts import render, redirect
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from items.models import Product_name, Items, Product_code, Technician
from django.db.models import F, Sum, ExpressionWrapper, IntegerField
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    items = Items.objects.all()[0:6]
    categories = Product_name.objects.all()
    tech=Technician.objects.all()
    items_count= Product_code.objects.all().count()
    itemscount= Items.objects.all().count()
    item_quantity= items_count - itemscount
    return render(request, 'core/index.html', {'items': items, 'categories': categories, 'tech':tech,'items_count':items_count, 'itemscount':itemscount, 'item_quantity':item_quantity})


def contact(request):
    return render(request, 'core/contact.html')

def items(request):
    query = request.GET.get('query', '')
    product_id = request.GET.get('Product_name', 0)
    tech_id = request.GET.get('Technician', 0)
    # tcategories = Technician.objects.all()
    # categories = Product_name.objects.all()
    items = Items.objects.filter(created_by = request.user)

    if product_id:
         items = items.filter(Product_name_id = product_id)
        
    if tech_id:
         items = items.filter(Technician_id = tech_id)

    # if query:
    #     items = items.filter(Q(Patient_name__icontains=query) | Q(id__icontains=query))
     
    return render(request, 'core/list.html', {'items': items,'query': query,  'product_id' : int(product_id),'tech_id' : int(tech_id),  })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})