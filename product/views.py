import json
import jwt
import requests

from django.views           import View
from django.http            import JsonResponse

from psr.settings           import SECRET_KEY, ALGORITHM
from account.models         import User, Count
from product.models         import ProductList
from utility.views          import login_required


class URLSimilarProductView(View):

    #@login_required
    def post(self, request):
        img_url                 = json.loads(request.body)['img_url']
        url                     = 'http://49.247.197.215:8885/getSimilarProducts?APIKEY=wecode-test&contentUrl='
        response                = requests.get(url+img_url)
        result                  = response.json()['result']
        grouped_results         = result['productGroupedResults']
        #user                    = kwargs['user']
        #Count.objects.create(user = user)
        result_box_lst = []
        
        result_box_lst = [{
            "coordinates": box['boundingPoly']['normalizedVertices'], 
            "product": [{
                "product_name"  : product["product"]["name"],
                "product_uri"   : product["product"]["img_uri"],
                "price"         : product["product"]["product_price"],
                "product_label1": product["product"]["productLabels"][1]["value"] if len(product["product"]["productLabels"]) > 1 else "",
                "product_label2": product["product"]["productLabels"][2]["value"] if len(product["product"]["productLabels"]) > 2 else "",
                "product_label3": product["product"]["productLabels"][3]["value"] if len(product["product"]["productLabels"]) > 3 else "",
                "score"         : product["score"]
                } for product in box['results'] if product["score"] >  0.25]
        } for box in grouped_results]

        return JsonResponse({"grouped_results": result_box_lst}, status=200)

class FileSimilarProductView(View):

    #@login_required
    def post(self, request):
        img                     = request.FILES['data']
        with img.open('rb') as f:
            #files = {'file': f}
            url                     = 'http://49.247.197.215:8885/getSimilarProducts?APIKEY=wecode-test'
            response                = requests.post(url, data=f)
            result                  = response.json()['result']
            grouped_results         = result['productGroupedResults']
            #user                    = kwargs['user']
            #Count.objects.create(user = user)
            result_box_lst = [{
                "coordinates": box['boundingPoly']['normalizedVertices'], 
                "product": [{
                    "product_name": product["product"]["name"],
                    "product_uri"   : product["product"]["img_uri"],
                    "price"         : product["product"]["product_price"],
                    "product_label1": product["product"]["productLabels"][1]["value"] if len(product["product"]["productLabels"]) > 1 else "",
                    "product_label2": product["product"]["productLabels"][2]["value"] if len(product["product"]["productLabels"]) > 2 else "",
                    "product_label3": product["product"]["productLabels"][3]["value"] if len(product["product"]["productLabels"]) > 3 else "",
                    "score"         : product["score"]
                    } for product in box['results'] if product["score"] >  0.25]
            } for box in grouped_results]

            return JsonResponse({"grouped_results": result_box_lst}, status=200)


class MainProductView(View):

    #@login_required
    def get(self, request):
        #user = kwargs['user']
        #Count.objects.create(user = user)
        
        product_lst = [{
            "product_name"  : product.product_name,
            "product_uri"   : product.img_url,
            "price"         : product.price_pc,
            "product_label1": product.cat_key[0],
            "product_label2": product.cat_key[1],
            "product_label3": product.cat_key[-2:]
        }for product in ProductList.objects.all().order_by('id')[300:350]]

        return JsonResponse({"product": product_lst})
