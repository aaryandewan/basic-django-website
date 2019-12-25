from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'


def item(request):
    return HttpResponse("This  is an item view.")

def info(request):
    return HttpResponse("I am loving this song called: Ngwa!")

def detail(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item' : item,
    }
    return render(request, 'food/detail.html', context)

#this is a class based view for create_item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image' ]#We only specify those fields which we want to be present in our form
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return redirect('')

def update_item(request, id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = item)
    if (form.is_valid()):
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item': item} )

def delete_item(request, id):
    item = Item.objects.get(id = id)

    if (request.method == 'POST'):
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item': item})
