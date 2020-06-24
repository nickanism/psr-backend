import json
import jwt
import bcrypt

from codesandwich.settings  import SECRET_KEY
from django.views           import View
from django.http            import HttpResponse, JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import User


class SignInView(View):s
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            if Customer.objects.filter(email = data['email']).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), Customer.objects.get(email = data['email']).password.encode('utf-8')):
                    token = jwt.encode({ 'id' : data['id'] }, SECRET_KEY, algorithm='HS256').decode('utf-8')
                    return JsonResponse({'token':token},status=200)
                return JsonResponse({'message':'INVALID_USER'},status=401)
            return JsonResponse({'message':'INVALID_USER'},status=401)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)