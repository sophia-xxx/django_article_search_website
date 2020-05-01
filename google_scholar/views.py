from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from google_scholar.forms import AuthorForm
from google_scholar.models import Author


class AuthorList(ListView):
    model=Author
    template_name = 'google_scholar/templates/bootstrap/author_list.html'

class AuthorDetail(View):
    def get(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        article_list=author.articles.all()
        return render(request,'google_scholar/author_detail.html',{'author':author,'article_list':article_list})

class AuthorCreate(CreateView):
    form_class=AuthorForm
    model=Author

class AuthorUpdate(UpdateView):
    form_class = AuthorForm
    model=Author
    template_name = 'google_scholar/author_form_update.html'

class AuthorDelete(DeleteView):
    model=Author
    success_url = reverse_lazy('author_list.html')




