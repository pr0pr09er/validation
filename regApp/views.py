from django.shortcuts import render, HttpResponse, redirect
from regApp import forms


def reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse(f"""
                                <h2>{name}, поздравляю с регистрацией!</h2>
                                <p>Вот ваши данные:</p>
                                <ol>
                                <li>Почта: {email}</li>
                                <li>Пароль: {password}</li>
                                </ol>                         
                            """)
    else:
        registration = forms.RegistrationForm()
        return render(request, 'reg.html', {'form': registration})


def enter(request):
    if request.method == 'POST':
        enter_form = forms.EnterForm(request.POST)
        if enter_form.is_valid():
            email = enter_form.cleaned_data['email']
            password = enter_form.cleaned_data['password']
            if email == 'User1' and password == '12345678':
                return HttpResponse('Поздравляю с успешным входом')
            else:
                return redirect('reg')
    else:
        enter_form = forms.EnterForm()
        return render(request, 'enter.html', {'form': enter_form})
