from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'record/main.html')

def login(request):
    return render(request,'registration/login.html')

def join(request):
    return render(request,'registration/join.html')

def reset_account(request):
    return render(request,'registration/reset_account.html')

def pop_hiphop(request):
    return render(request,'record/pop_hiphop.html')

def pop_rnb(request):
    return render(request,'record/pop_rnb.html')

def kpop_indi(request):
    return render(request,'record/kpop_indi.html')

def kpop_hiphop(request):
    return render(request,'record/kpop_hiphop.html')

def ost(request):
    return render(request,'record/ost.html')

def cart(request):
    return render(request,'payment/cart.html')

def order(request):
    return render(request,'payment/order.html')
