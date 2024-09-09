from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  # Subclass for UserCreation
  class Meta:

    model=CustomUser

    # username, email, password, password confirmation
    fields=('username', 'email', 'password1','password2')