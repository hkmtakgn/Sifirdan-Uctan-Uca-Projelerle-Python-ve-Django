from django.shortcuts import render
from .products_database import twenty_picsum

# Create your views here.

def pro_views (request):
        for item in twenty_picsum:
            pic_id = item['id']
            pic_url = item['url']
            context = dict (
                   pic_id=pic_id,
                   pic_url=pic_url,
                   twenty_picsum=twenty_picsum,
            )
        return render (request,"products/products.html",context)

def detail_pro_view(request, product_id):
    # Ürün listesinde id'ye göre filtreleme yapıyoruz
    product = next((item for item in twenty_picsum if item['id'] == product_id), None)
    
    if product:
        # Ürün bulunduysa detayları gönderiyoruz
        context = {
            'pic_id': product['id'],
            'pic_url': product['url'],
        }
        return render(request, "products/detail_product.html", context)
    else:
        # Ürün bulunamadıysa 404 sayfası veya hata mesajı döndürebilirsiniz
        return render(request, "404.html")
