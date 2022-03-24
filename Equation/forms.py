from django import forms


class UserForm(forms.Form):
    a = forms.FloatField(label='Значение а')
    b = forms.FloatField(label='Значение b')
    c = forms.FloatField(label='Значение c')
