from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Введите имя',
                           widget=forms.TextInput(attrs={'class': 'registration--input', 'placeholder': 'Иван'}))
    email = forms.EmailField(label='Введите почту',
                             widget=forms.TextInput(
                                 attrs={'class': 'registration--input', 'placeholder': 'example@gmail.com'}))
    password = forms.CharField(label='Введите пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'registration--input', 'placeholder': '123456'}))


class EnterForm(forms.Form):
    email = forms.CharField(label='Введите почту',
                             widget=forms.TextInput(
                                 attrs={'class': 'enter--input', 'placeholder': 'example@gmail.com'}))
    password = forms.CharField(label='Введите пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'registration--input', 'placeholder': '123456'}))
