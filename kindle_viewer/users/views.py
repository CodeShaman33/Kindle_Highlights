from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


'''this is a view function for logging in by app user'''

def register(request):
    '''New  user users'''
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)

            return redirect('knowledge:index')

    return render(request, 'registration/register.html', {'form': form})


'''function that displays info of logging out '''
def logout(request):

    return render(request, 'users/logout.html')