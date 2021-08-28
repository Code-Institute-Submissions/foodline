from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(request,
                                 (f'Updated {product.name} - '
                                  f'{ripeness} quantity to '
                                  f'{cart[item_id]["items_by_ripeness"][ripeness]}'))
            else:
                cart[item_id]['items_by_ripeness'][ripeness] = quantity
                messages.success(request,
                                 (f'Added {product.name} - '
                                  f'{ripeness} to your cart'))
        else:
            cart[item_id] = {'items_by_ripeness': {ripeness: quantity}}
            messages.success(request,
                             (f'Added {product.name} - '
                              f'{ripeness} to your cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    ripeness = None
    if 'product_ripe' in request.POST:
        ripeness = request.POST['product_ripe']
    cart = request.session.get('cart', {})

    if ripeness:
        if quantity > 0:
            cart[item_id]['items_by_ripeness'][ripeness] = quantity
            messages.success(request,
                             (f'Updated {product.name} - '
                              f'{ripeness} quantity to '
                              f'{cart[item_id]["items_by_ripeness"][ripeness]}'))
        else:
            del cart[item_id]['items_by_ripeness'][ripeness]
            if not cart[item_id]['items_by_ripeness']:
                cart.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} - '
                              f'{ripeness} from your cart'))
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'{product.name} Removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        ripeness = None
        if 'product_ripe' in request.POST:
            ripeness = request.POST['product_ripe']
        cart = request.session.get('cart', {})

        if ripeness:
            del cart[item_id]['items_by_ripeness'][ripeness]
            if not cart[item_id]['items_by_ripeness']:
                cart.pop(item_id)
                messages.success(request,
                                 (f'Removed {product.name} - '
                                  f'{ripeness} from your cart'))
        else:
            cart.pop(item_id)
            messages.success(request, f'{product.name} Removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
