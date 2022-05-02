from django.shortcuts import render,redirect
from app.form import CelsForm
from app.models import Cels
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    data = {}
    # data['db'] = Cels.objects.all()
    all = Cels.objects.all()
    search = request.GET.get('search')
    if search:
        data['db'] = Cels.objects.filter(modelo__icontains=search)
    else:
        paginator = Paginator(all, 3)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CelsForm()
    return render(request, 'form.html', data)

def create(request):
    form = CelsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Cels.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cels.objects.get(pk=pk)
    data['form'] = CelsForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cels.objects.get(pk=pk)
    form = CelsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Cels.objects.get(pk=pk)
    db.delete()
    return redirect('home')

# Create your views here.
