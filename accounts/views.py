from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
  form_class=CustomUserCreationForm
  # template to render
  template_name="signup.html"
  # redirected url after sign up
  success_url=reverse_lazy('accounts:signup_success')

  def form_valid(self, form):
    '''
    paremeters:
      form(django.forms.Form):
        CustomerUserCreationForm object
      return:
        HttpResponseRedirect object:
          Redirecting to success_url by returing the value from super class of form_valid()
    '''
    user=form.save()
    self.object=user

    return super().form_valid(form)

class SignUpSuccessView(TemplateView):
  template_name="signup_success.html"