from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to render shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A view to add specific quantity of a product to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ A view to remove product from shopping bag """

    bag = request.session.get('bag', {})

    if item_id in bag:
        bag.pop(item_id)
        request.session['bag'] = bag
    
    return redirect('view_bag')