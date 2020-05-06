from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from google_scholar.forms import AuthorForm, JournalForm, ArticleForm, TopicForm
from google_scholar.models import Author, Journal, Article, Topic


# index
class IndexView(View):
    def get(self,request):
        return render(request, 'google_scholar/index.html', {'journal_list':Journal.objects.all()})


# author
class AuthorList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=Author
    template_name = 'google_scholar/author_list.html'
    permission_required = 'google_scholar.view_author'

class AuthorDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.view_author'
    def get(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        article_list=author.articles.all()
        return render(request, 'google_scholar/author_detail.html', {'author':author, 'article_list':article_list})

class AuthorCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'google_scholar.add_author'
    form_class=AuthorForm
    model=Author
    template_name = 'google_scholar/author_form.html'

class AuthorUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'google_scholar.change_author'
    form_class = AuthorForm
    model=Author
    template_name = 'google_scholar/author_form_update.html'

class AuthorDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.delete_author'

    def get(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        article_list=author.articles.all()
        if article_list.count()>0:
            return render(
                request,
                'google_scholar/author_refuse_delete.html',
                {
                    'author':author,
                    'article_list':article_list
                }
            )
        else:
            return render(
                request,
                'google_scholar/author_confirm_delete.html',
                {'author':author}
            )
    # deal with exception
    def post(self,request,pk):
        author=get_object_or_404(Author,pk=pk)
        author.delete()
        return redirect('author_list_url')


# journal
class JournalList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'google_scholar.view_journal'
    model=Journal
    template_name = 'google_scholar/journal_list.html'

class JournalDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.view_journal'
    def get(self,request,pk):
        journal=get_object_or_404(Journal,pk=pk)
        article_list=journal.articles.all()
        return render(request, 'google_scholar/journal_detail.html', {'journal':journal, 'article_list':article_list})

class JournalCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'google_scholar.add_journal'
    form_class=JournalForm
    model=Journal
    template_name = 'google_scholar/journal_form.html'

class JournalUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'google_scholar.change_journal'
    form_class = JournalForm
    model=Journal
    template_name = 'google_scholar/journal_form_update.html'

class JournalDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.delete_journal'
    def get(self, request, pk):
        journal = get_object_or_404(Journal, pk=pk)
        articles = journal.articles.all()
        if articles.count() > 0:
            return render(
                request,
                'google_scholar/journal_refuse_delete.html',
                {
                    'journal': journal,
                    'articles': articles
                }
            )
        else:
            return render(
                request,
                'google_scholar/journal_confirm_delete.html',
                {'journal': journal}
            )

    # deal with exception
    def post(self, request, pk):
        journal = get_object_or_404(Journal, pk=pk)
        journal.delete()
        return redirect('journal_list_url')



# article
class ArticleList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'google_scholar.view_article'
    model=Article
    template_name = 'google_scholar/article_list.html'

class ArticleDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.view_article'
    def get(self,request,pk):
        article=get_object_or_404(Article,pk=pk)
        author=article.author
        journal=article.journal
        return render(request, 'google_scholar/article_detail.html',
                      {'article':article,
                       'author':author,
                       'journal':journal})

class ArticleCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'google_scholar.add_article'
    form_class=ArticleForm
    model=Article
    template_name = 'google_scholar/article_form.html'

class ArticleUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'google_scholar.change_article'
    form_class = ArticleForm
    model=Article
    template_name = 'google_scholar/article_form_update.html'

class ArticleDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'google_scholar.delete_article'
    model=Article
    template_name = 'google_scholar/article_confirm_delete.html'
    success_url = reverse_lazy('article_list_url')

# topic
class TopicList(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.view_topic'
    def get(self, request):
        return render(request, 'google_scholar/topic_list.html', {'topic_list': Topic.objects.all()})

class TopicDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.view_topic'
    def get(self,request,pk):
        topic=get_object_or_404(Topic,pk=pk)
        topic_list=Topic.objects.all()
        article_list=topic.articles.all()
        author_list=topic.authors.all()
        return render(request, 'google_scholar/topic_detail.html',
                      {'topic':topic,'article_list':article_list,'author_list':author_list,'topic_list':topic_list})

class TopicCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'google_scholar.add_topic'
    form_class=TopicForm
    model=Topic
    template_name = 'google_scholar/topic_form.html'

class TopicUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'google_scholar.change_topic'
    form_class = TopicForm
    model=Topic
    template_name = 'google_scholar/topic_form_update.html'

class TopicDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'google_scholar.delete_topic'
    def get(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        articles = topic.articles.all()
        if articles.count() > 0:
            return render(
                request,
                'google_scholar/topic_refuse_delete.html',
                {
                    'topic': topic,
                    'articles': articles
                }
            )
        else:
            return render(
                request,
                'google_scholar/topic_confirm_delete.html',
                {'topic': topic}
            )

    # deal with exception
    def post(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        topic.delete()
        return redirect('topic_list_url')


def search(request):
    template='google_scholar/article_list.html'
    query=request.GET.get('q')
    article_list=Article.objects.filter(Q(title__icontains=query))
    context={
        'article_list':article_list
    }
    return render(request,template,context)