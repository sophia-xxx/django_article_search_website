from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from google_scholar.forms import AuthorForm, JournalForm, ArticleForm
from google_scholar.models import Author, Journal, Article


# index
class IndexView(View):
    def get(self,request):
        return render(request,'bootstrap/index.html',{'journal_list':Journal.objects.all()})


# author
class AuthorList(ListView):
    model=Author
    template_name = 'bootstrap/author_list.html'

class AuthorDetail(View):
    def get(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        article_list=author.articles.all()
        return render(request,'bootstrap/author_detail.html',{'author':author,'article_list':article_list})

class AuthorCreate(CreateView):
    form_class=AuthorForm
    model=Author
    template_name = 'bootstrap/author_form.html'

class AuthorUpdate(UpdateView):
    form_class = AuthorForm
    model=Author
    template_name = 'bootstrap/author_form_update.html'

class AuthorDelete(DeleteView):
    model=Author
    template_name = 'bootstrap/author_confirm_delete.html'
    success_url = reverse_lazy('author_list_url')



# journal
class JournalList(ListView):
    model=Journal
    template_name = 'bootstrap/journal_list.html'

class JournalDetail(View):
    def get(self,request,pk):
        journal=get_object_or_404(Journal,pk=pk)
        article_list=journal.articles.all()
        return render(request,'bootstrap/journal_detail.html',{'journal':journal,'article_list':article_list})

class JournalCreate(CreateView):
    form_class=JournalForm
    model=Journal
    template_name = 'bootstrap/journal_form.html'

class JournalUpdate(UpdateView):
    form_class = JournalForm
    model=Journal
    template_name = 'bootstrap/journal_form_update.html'

class JournalDelete(DeleteView):
    model=Journal
    template_name = 'bootstrap/journal_confirm_delete.html'
    success_url = reverse_lazy('journal_list_url')



# article
class ArticleList(ListView):
    model=Article
    template_name = 'bootstrap/article_list.html'

class ArticleDetail(View):
    def get(self,request,pk):
        article=get_object_or_404(Article,pk=pk)
        author=article.author
        journal=article.journal
        return render(request,'bootstrap/article_detail.html',
                      {'article':article,
                       'author':author,
                       'journal':journal})

class ArticleCreate(CreateView):
    form_class=ArticleForm
    model=Article
    template_name = 'bootstrap/article_form.html'

class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model=Article
    template_name = 'bootstrap/article_form_update.html'

class ArticleDelete(DeleteView):
    model=Article
    template_name = 'bootstrap/article_confirm_delete.html'
    success_url = reverse_lazy('article_list_url')

