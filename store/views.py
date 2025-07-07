from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import SignUpForm
import json

# Product listing
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# Product detail
@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})

# Add to cart
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})

    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1
    else:
        cart[str(pk)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image': str(product.image)  # Ensures it's serialized for session
        }

    request.session['cart'] = cart
    return redirect('view_cart')

# View cart
@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})

# Update cart quantity
@login_required
def update_cart(request, pk):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            cart[str(pk)]['quantity'] = quantity
            request.session['cart'] = cart
    return redirect('view_cart')

# Remove from cart
@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
    request.session['cart'] = cart
    return redirect('view_cart')

# Checkout and save order
@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    if cart:
        Order.objects.create(
            user=request.user,
            items=json.dumps(cart),
            total=total
        )
    request.session['cart'] = {}
    return render(request, 'checkout.html')

# Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# My orders view
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Parse JSON into Python dictionaries
    for order in orders:
        order.parsed_items = json.loads(order.items)

    return render(request, 'my_orders.html', {'orders': orders})