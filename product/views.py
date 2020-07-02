import json
import jwt
import requests

from django.views           import View
from django.http            import JsonResponse

from psr.settings           import SECRET_KEY, ALGORITHM
from account.models         import User
from utility.views          import login_required

class URLSimilarProductView(View):
    
    def post(self, request):
        
        img_url                 = json.loads(request.body)['img_url']
        url                     = 'http://49.247.197.215:8885/getSimilarProducts?APIKEY=wecode-test&contentUrl='
        response                = requests.get(url+img_url)
        result                  = response.json()['result']
        product_lst             = result['productGroupedResults'][0]['results']
        high_rating_product_lst = [{
            "product_name"  : product["product"]["name"],
            "product_uri"   : product["product"]["img_uri"],
            "price"         : product["product"]["product_price"],
            "product_label1": product["product"]["productLabels"][1]["value"],
            "product_label2": product["product"]["productLabels"][2]["value"],
            "product_label3": product["product"]["productLabels"][3]["value"],
            "score"         : product["score"]
        } for product in product_lst if product["score"] > 0.26]
        final_lst = [dict(t) for t in {tuple(d.items()) for d in high_rating_product_lst}]

        return JsonResponse({"product": final_lst})

class FileSimilarProductView(View):

    def post(self, request):
        img                     = request.FILES['data']
        with img.open('rb') as f:
            #files = {'file': f}
            url                     = 'http://49.247.197.215:8885/getSimilarProducts?APIKEY=wecode-test'
            response                = requests.post(url, data=f)
            result                  = response.json()['result']
            product_lst             = result['productGroupedResults'][0]['results']
            high_rating_product_lst = [{
                "product_name"  : product["product"]["name"],
                "product_uri"   : product["product"]["img_uri"],
                "price"         : product["product"]["product_price"],
                "product_label1": product["product"]["productLabels"][1]["value"],
                "product_label2": product["product"]["productLabels"][2]["value"],
                "product_label3": product["product"]["productLabels"][3]["value"],
                "score"         : product["score"]
            } for product in product_lst if product['score'] > 0.26]

            final_lst = [dict(t) for t in {tuple(d.items()) for d in high_rating_product_lst}]

            return JsonResponse({"product": final_lst})
