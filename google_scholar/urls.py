
from django.contrib import admin
from django.urls import path

from google_scholar.views import AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete, JournalList, \
    JournalDetail, JournalCreate, JournalUpdate, JournalDelete, ArticleDetail, ArticleCreate, ArticleUpdate, \
    ArticleDelete, ArticleList, IndexView, TopicList, TopicDetail, TopicCreate, TopicUpdate, TopicDelete
from django.views.generic import TemplateView

urlpatterns = [

    path('index/', IndexView.as_view(),name='index_url'),

    # author
    path('author/',AuthorList.as_view(),name='author_list_url'),
    path('author/<int:pk>/',AuthorDetail.as_view(),name='author_detail_url'),
    path('author/create/',AuthorCreate.as_view(),name='author_create_url'),
    path('author/<int:pk>/update/',AuthorUpdate.as_view(),name='author_update_url'),
    path('author/<int:pk>/delete',AuthorDelete.as_view(),name='author_delete_url'),

    # article
    # list-detail-create-delete-update
    path('article/',ArticleList.as_view(),name='article_list_url' ),
    path('article/<int:pk>/',ArticleDetail.as_view(),name='article_detail_url'),
    path('article/create/',ArticleCreate.as_view(),name='article_create_url'),
    path('article/<int:pk>/update/',ArticleUpdate.as_view(),name='article_update_url'),
    path('article/<int:pk>/delete',ArticleDelete.as_view(),name='article_delete_url'),

    # journal
    path('journal/',JournalList.as_view(),name='journal_list_url'),
    path('journal/<int:pk>/',JournalDetail.as_view(),name='journal_detail_url'),
    path('journal/create/',JournalCreate.as_view(),name='journal_create_url'),
    path('journal/<int:pk>/update/',JournalUpdate.as_view(),name='journal_update_url'),
    path('journal/<int:pk>/delete',JournalDelete.as_view(),name='journal_delete_url'),

    # topic
    path('topic/',TopicList.as_view(),name='topic_list_url'),
    path('topic/<int:pk>/',TopicDetail.as_view(),name='topic_detail_url'),
    path('topic/create/',TopicCreate.as_view(),name='topic_create_url'),
    path('topic/<int:pk>/update/',TopicUpdate.as_view(),name='topic_update_url'),
    path('topic/<int:pk>/delete',TopicDelete.as_view(),name='topic_delete_url'),
]