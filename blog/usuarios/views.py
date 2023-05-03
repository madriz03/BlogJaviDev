from django.shortcuts import render, redirect
from  .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso, puedes iniciar sesion")
            return redirect('login')
        else:
            messages.error(request, "No se pudo completar el registro")
            return redirect('register')

    else:
        
        form = UserRegisterForm()
        
    return render(request, 'usuarios/register.html', {'form': form})