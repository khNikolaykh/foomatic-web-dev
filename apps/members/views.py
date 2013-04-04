from django.shortcuts import render
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
	pass
    else:
	form = forms.SignupForm()

    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'members/profile.html', {'user': request.user})
