from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import OrderListAddProductForm
from .orderlist import OrderList
from shop.models import Product


@require_POST
def orderlist_add(request, product_id):
    orderlist = OrderList(request)
    product = Product.objects.get(id=product_id)
    form = OrderListAddProductForm(request.Post)
    if form.is_valid():
        cd = form.cleaned_data
        orderlist.add(product=product,
                      count=cd['count'],
                      update_count=cd['update'])
    return redirect('orderlist:orderlist_detail')


def orderlist_remove(request, product_id):
    ordelist = OrderList(request)
    product = Product.objects.get(id=product_id)
    ordelist.remove(product)
    return redirect('orderlist:orderlist-detail')


def orderlist_detail(request):
    orderlist = OrderList(request)
    return render(request, 'orderlist/orderlist-detail.html', {'orderlist': orderlist})
