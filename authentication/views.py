from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ho')
    else:
        form =CustomUserCreationForm()
    return render(request, 't.html', {'form': form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			request.session['user'] = user.id
			
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("ho")
			 
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login .html", context={"login_form":form})



# Create your views here.
@login_required(login_url='/login/')
def homepage(request):
    return render(request,'t2.html')


def logout_request(request):
	# del request.session['user']
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")




