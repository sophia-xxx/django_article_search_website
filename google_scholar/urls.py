
from django.contrib import admin
from django.urls import path

from google_scholar.views import AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete
from django.views.generic import TemplateView

urlpatterns = [
    # author
    path('author/',AuthorList.as_view(),name='author_list_url'),
    path('author/<int:pk>/',AuthorDetail.as_view(),name='author_detail_url'),
    path('author/create/',AuthorCreate.as_view(),name='author_create_url'),
    path('author/<int:pk>/update/',AuthorUpdate.as_view(),name='author_update_url'),
    path('author/<int:pk>/delete',AuthorDelete.as_view(),name='author_delete_url'),

    path('index/',TemplateView.as_view(template_name='bootstrap/index.html'))
    # article
    # list-detail-create-delete-update


    # topic
    # list-detail-create-delete-update

    # journal
    # list-detail-create-delete-update
]