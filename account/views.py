import json
import jwt
import bcrypt

from psr.settings                   import SECRET_KEY
from django.views                   import View
from django.http                    import HttpResponse, JsonResponse
from django.core.validators         import validate_email
from django.core.exceptions         import ValidationError
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib                 import messages
from django.http                    import HttpResponseRedirect
from django.contrib.auth.decorator  import login_required
from django.contrib.auth            import login, logout, authenticate
from django.contrib.auth.views      import LoginView

from .models import User


class LoginView(LoginView):
    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                messages.add_message(request, messages.SUCCESS, "Welcome back, {}".format(user))

                login(request, user)

                token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                
                return JsonResponse({'token': token}, status=200) 