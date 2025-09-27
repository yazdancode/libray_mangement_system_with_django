from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "نام کاربری"}
        ),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "رمز عبور"}
        ),
    )
