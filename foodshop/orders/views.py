from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from orderlist.orderlist import OrderList


def create_order(request):
    orderlist = OrderList(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in orderlist:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['count'])
            orderlist.clear()
            return render(request, 'orders/order_created.html', {'orders': order})
    else:
        form = OrderForm()
        return render(request, 'orders/order_create.html', {'orderlist': orderlist, 'form': form})
