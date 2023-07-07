from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from .forms import EditItemForm, NewItemForm
from .models import Items, Product_name, Technician, Product_code


def index(request):
    items = Items.objects.all()[0:6]
    categories = Product_name.objects.all()
    tech=Technician.objects.all()   
    return render(request, 'items/items.html', {'items': items, 'categories': categories, 'tech':tech,})


def items(request):
    query = request.GET.get('query', '')
    product_id = request.GET.get('Product_name', 0)
    tech_id = request.GET.get('Technician', 0)
    tcategories = Technician.objects.all()
    categories = Product_name.objects.all()
    items = Items.objects.filter(is_sold=False)

    if product_id:
         items = items.filter(Product_name_id = product_id)
    
    if tech_id:
          items = items.filter(Technician_id = tech_id)
        
    # if tech_id:
    #     items = items.filter(Technician_id = tech_id)

    if query:
        items = items.filter(Q(Patient_name__icontains=query) | Q(id__icontains=query))
    
    if query:
         items = items.filter(Q(Technician__icontains=query) | Q(id__icontains=query))
     
    return render(request, 'items/items.html', {'items': items,'query': query,'tcategories': tcategories, 'categories': categories,   'product_id' : int(product_id), 'tech_id' : int(tech_id),  })

# 'categories': tcategories,
# 'product_id' : int(product_id),
# Create your views here.

# def techy(request):
#     tquery = request.GET.get('query', '')
#     # product_id = request.GET.get('Product_name', 0)
#     tech_id = request.GET.get('Technician', 0)
#     #categories = Product_name.objects.all()
#     pcategories = Technician.objects.all()
#     items = Items.objects.filter(is_sold=False)

#     if tech_id:
#          items = items.filter(Technician_id = tech_id)
        
#     # if tech_id:
#     #     items = items.filter(Technician_id = tech_id)

#     if tquery:
#         items = items.filter(Q(Technician__icontains=tquery) | Q(id__icontains=tquery))
     
#     return render(request, 'items/items.html', {'items': items,'query': tquery,'categories': pcategories,  'tech_id' : int(tech_id),  })






def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(Technician=item.Technician, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'items/detail.html', {'item': item, "related_items": related_items,})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.phone_number = '+917447374275'
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'items/form.html', {'form': form, 'title': 'Patient Details',})


@login_required
def edit(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by = request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {'form': form, 'title': 'Edit item',})


@login_required
def delete(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by = request.user)
    item.delete()
    
    return redirect('dashboard:index')

def load_cities(request):
    Product_name_id = request.GET.get('Product_name_id')
    cities = Product_code.objects.filter(Product_name_id=Product_name_id).all()
    return render(request, 'items/city_dropdown_list_options.html', {'cities': cities})
    