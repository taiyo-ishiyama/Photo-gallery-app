from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from .models import PhotoPost

from django.views.generic import DetailView, DeleteView

class IndexView(ListView):
  template_name='index.html'
  queryset = PhotoPost.objects.order_by('-posted_at')
  # number of records per page
  paginate_by = 9

# only limited to logined users
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    # template to render
    template_name = "post_photo.html"
    # redirect url after registration
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form): # overide from CreateView class
        # get posted data with commit=False
        postdata = form.save(commit=False)

        postdata.user = self.request.user
        postdata.save()
        # return (HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
  template_name ='post_success.html'

class CategoryView(ListView):
    # render index.html
    template_name ='index.html'
    # number of records per page
    paginate_by = 9

    def get_queryset(self):
      category_id = self.kwargs['category']
      categories = PhotoPost.objects.filter(
        category=category_id).order_by('-posted_at')
      return categories

class UserView(ListView):
    # render index.html
    template_name ='index.html'
    # number of records each page
    paginate_by = 9

    def get_queryset(self):
      user_id = self.kwargs['user']
      user_list = PhotoPost.objects.filter(
        user=user_id).order_by('-posted_at')
      return user_list

class DetailView(DetailView):
    # render post.html
    template_name ='detail.html'
    model = PhotoPost

class MypageView(ListView):
    # render mypage.html
    template_name ='mypage.html'
    paginate_by = 9

    def get_queryset(self):
      queryset = PhotoPost.objects.filter(
        user=self.request.user).order_by('-posted_at')
      return queryset

class PhotoDeleteView(DeleteView):
    model = PhotoPost
    # render photo_detail.html
    template_name ='photo_delete.html'
    # redirect to mypage upon the completion
    success_url = reverse_lazy('photo:mypage')

    def delete(self, request, *args, **kwargs):
      return super().delete(request, *args, **kwargs)