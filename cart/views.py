from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    ripeness = None
    if 'product_ripe' in request.POST:
        ripeness = request.POST['product_ripe']
    cart = request.session.get('cart', {})

    if ripeness:
        if item_id in list(cart.keys()):
            if ripeness in cart[item_id]['items_by_ripeness'].keys():
                cart[item_id]['items_by_ripeness'][ripeness] += quantity
            else:
                cart[item_id]['items_by_ripeness'][ripeness] = quantity
        else:
            cart[item_id] = {'items_by_ripeness': {ripeness: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
