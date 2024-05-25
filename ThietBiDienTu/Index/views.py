from django.shortcuts import render, get_object_or_404

# Import model
from .models import Product
from .models import Member
from .models import Customer
from .models import Category
from django.http import HttpResponse 

# Create your views here.
#Đăng ký
def register(request):
    context = {}
    return render(request, 'page/Register.html', context)
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

