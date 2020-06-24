import json
import jwt

from django.views                   import View
from django.http                    import JsonResponse, HttpResponse
from django.utils.datastructures    import MultiValueDictKeyError


def login_required(func):
        def wrapper(self, request, *args, **kwargs):

            try:
                header_token            = request.headers['Authorization']
                if header_token         == None:
                    return JsonResponse({"message": "THE TOKEN IS EMPTY"}, status=400)
                decoded_token           = jwt.decode(header_token, SECRET_KEY, algorithm=ALGORITHM)
                user                    = User.objects.get(id=decoded_token['id'])
                user_id                 = user.id
                kwargs['user']          = user
                kwargs['user_id']       = user_id
                if User.objects.filter(id=decoded_token['id']).exists():
                    return func(self, request, *args, **kwargs)
                else:
                    return JsonResponse({"message": "THE USER DOES NOT EXIST"})
            except jwt.DecodeError:
                return JsonResponse({"message": "WRONG_TOKEN!"}, status=403)
            except KeyError:
                return JsonResponse({"message": "KEY ERROR"}, status=403)
        return wrapper

