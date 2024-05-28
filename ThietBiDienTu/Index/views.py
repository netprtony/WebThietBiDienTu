from django.shortcuts import render, get_object_or_404, redirect

# Import model

from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
# Create your views here.
#Đăng ký
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    
    context = {'form':form}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu không đúng!')
    context = {}
    return render(request, 'pages/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')    

# Thành viên
def Member_list(request):
    data={
		'DM_ThanhVien':Customer.objects.all(),

	} 
    return render(request, 'pages/thanhviennhom.html', data)

# Danh sách sản phẩm theo bảng
def product_list_f(request):
    data={
		'DM_SanPham':Product.objects.all(),
	} 
    return render(request, 'pages/DanhSachSanPham.html', data)
# Danh sách sản phẩm theo card
def product_f(request):
    data={
		'DM_SanPham':Product.objects.all(),
	} 
    return render(request, 'pages/index.html', data)

# Tìm kiếm thông tin
def search_product(request):
    query = request.GET.get('q')
    product = None
    if query:
        product = Product.objects.filter(name__icontains=query).first()
    return render(request, 'pages/ChiTietSanPham.html', {'product': product})

#Loai
def Loai_list(request):
    data={
		'DM_Loai':Category.objects.all(),
	} 
    return render(request, 'pages/DanhSachLoai.html', data)

#Chi tiết sản phẩm
def product_detail(request, product_id):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'pages/ChiTietSanPham.html', {'product': product})



