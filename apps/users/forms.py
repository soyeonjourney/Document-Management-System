from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'font-family: cursive'}))
    password1 = forms.CharField(max_length=256,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'font-family: cursive'}))
    password2 = forms.CharField(max_length=256,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'style': 'font-family: cursive'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'font-family: cursive'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'font-family: cursive'}))
    password = forms.CharField(max_length=256,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'font-family: cursive'}))
