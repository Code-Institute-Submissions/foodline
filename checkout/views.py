from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Shopping Cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JTXxiFXVFcygOp2B11NvJw3PToYeEndat2cX7vFE07A1uJnxcxguN8RmBRdZiz2Fhk2Dx185kV6ImHQ2HuTdPMA00rjoq5NUE',
        'cliet_secret': 'test client secret',
    }

    return render(request, template, context)
