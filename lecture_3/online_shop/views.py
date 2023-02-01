from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from online_shop.models import Category, Product


def get_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]

    return JsonResponse(data=categories_json, status=200, safe=False)


def get_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]

    return JsonResponse(data=products_json, status=200, safe=False)


def get_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category_json = category.to_json()
    except Category.DoesNotExist as e:
        return JsonResponse(data={ 'message': "Category does not exist"}, status=404)

    return JsonResponse(data=category_json, status=200)


def get_category_products(request, pk):
    try:
        category = Category.objects.get(id=pk)
        products = category.product_set.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(data=products_json, status=200, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse(data={'message': "Category does not exist"}, status=404)


def get_product_of_category(request, pk1, pk2):
    try:
        category = Category.objects.get(id=pk1)
        try:
            product = category.product_set.get(id=pk2)
            print(product)
            return JsonResponse(data=product.to_json(), status=200, safe=False)
        except Product.DoesNotExist as e:
            return JsonResponse(data={'message': "Product with ID: {} does not belong to category {}".format(pk2, category.name)}, status=404, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse(data={'message': "Category does not exist"}, status=404, safe=False)


def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product_json = product.to_json()
    except Category.DoesNotExist as e:
        return JsonResponse(data={'message': "Product does not exist"}, status=404)

    return JsonResponse(data=product_json, status=200)


/companies/id/calculate-tax