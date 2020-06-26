import json
import jwt
import requests

from django.views           import View
from django.http            import JsonResponse

from psr.settings           import SECRET_KEY, ALGORITHM
from account.models         import User
from utility.views          import login_required

class SimilarProductView(View):
    def get(self, request):
        import pdb; pdb.set_trace()
        img_url                 = json.loads(request.body)['img_url']
        url                     = 'http://49.247.197.215:8885/getSimilarProducts?APIKEY=wecode-test&contentUrl='
        response                = requests.get(url+img_url)
        result                  = response.json()['result']
        product_lst             = result['productGroupedResults'][0]['results']
        high_rating_product_lst = [{
            "product_name"  : product["name"] if product["name"] else "",
            "product_uri"   : product["img_uri"],
            "product_label1": product["productLabels"][1]["value"],
            "product_label2": product["productLabels"][2]["value"],
            "product_label3": product["productLabels"][3]["value"],
            "score"         : product["score"]
        } for product in product_lst if product['score'] > 0.25]

        return JsonResponse({"product": high_rating_product_lst})

    def post(self, request):
        pass