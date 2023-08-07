from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your forms here.

class AccountUsers(UserCreationForm):
	email = forms.EmailField(required=True)
	telephone = forms.CharField(max_length=20, required=True)  # Add the telephone field

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")
	def save(self, commit=True):
		user = super(AccountUsers, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
