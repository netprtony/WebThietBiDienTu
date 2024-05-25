from django.urls import path


from . import views # call to url_shortener/views.py 
urlpatterns = [ 
    path('', views.product_f, name='index'), 
    path('Member_list/', views.Member_list, name='Member_list'),
    path('products_list/', views.product_list_f, name='products_list'),
    path('products/', views.product_f, name='products'),
    path('loai_list/', views.Loai_list, name='loai_list'),
    path('product/<str:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search_product, name='search_product'),
    path('search/', views.register, name='register'),
] 