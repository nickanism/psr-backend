import json
import jwt

from psr.settings                   import SECRET_KEY
from django.http                    import HttpResponse, JsonResponse
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib                 import messages
from django.contrib.auth            import login, logout, authenticate
from django.utils.decorators        import method_decorator
from django.views.decorators.csrf   import csrf_exempt
from django.views                   import View
from braces.views                   import CsrfExemptMixin

from .models    import User
from .forms     import UserCreationForm


class LoginView(CsrfExemptMixin, View):
    
    def post(self, request):
        form = AuthenticationForm(data = request.POST)
            
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            messages.add_message(request, messages.SUCCESS, "Welcome back, {}".format(user))

            login(request, user)

            token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
            
            return JsonResponse({'token': token}, status=200)

        return JsonResponse({'message': "Incorrect email/password"})

class SignupView(CsrfExemptMixin, View):
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            
            if user is not None: 
                login(request, user)
                
                token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')

                return JsonResponse({'message': 'SUCCESS', 'token': token})
            return JsonResponse({'message': 'SOMETHING WENT WRONG'}, status = 400)

        return JsonResponse({'message': 'INVALID FORM'}, status = 400)