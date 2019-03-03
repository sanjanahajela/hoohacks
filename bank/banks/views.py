from django.http import HttpResponse
from .forms import LoginForm
from .models import Customer, Account, Authenticator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def Login(request):
	if (request.method == 'POST'):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			try:
				user = Customer.objects.get(email = request.POST['email'])
			except:
				return JsonResponse({'ok': False, 'result': "You do not currently have an account with that email."}, status=400)

			if check_password(request.POST['password'], user.password):
				authenticator = hmac.new(
					key = settings.SECRET_KEY.encode('utf-8'),
					msg = os.urandom(32),
					digestmod = 'sha256',
				).hexdigest()

			authent = Authenticator(user_id = users.email, authenticator = authenticator)
			authent.save()

			authenticator = authent.authenticator
			response.set_cookie("auth", authenticator)
			return render(request, 'home.html')

	else:
		login_form = LoginForm()
		return render(request, 'login.html', {'form':login_form})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")