from django.shortcuts import render
from django.http import HttpResponse
import shopify

def index(request):
	shop_url = "https://%s:%s@dibilopmentshap.myshopify.com/admin" % ("49aeb2871ca1a1b7c4d63e38be27dcbc", "7edac36ddfe7ef04751129a7262475c5")
	shopify.ShopifyResource.set_site(shop_url)
	shop = shopify.Shop.current()
	# Create a new product
	new_product = shopify.Product()
	new_product.title = "Kanye West"
	new_product.product_type = "Rapper"
	new_product.vendor = "Wife got Mugged"
	success = new_product.save()
	return HttpResponse("Hello, world. You're at the polls index.")