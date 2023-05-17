from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class ForHomepage(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    # Se não quiser que seja obrigatorio email = forms.EmailField(required=False)
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')


