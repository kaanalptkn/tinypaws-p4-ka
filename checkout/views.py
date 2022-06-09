from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KziLUAiTYKkxkcCqIeSwpAJOhjsesgHaOGAgLd1QR4VHkb3xDFyqB8evht8jQUR9TLu2y7YkePSO3whqIbWyOQ300Fjwg4IVW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)