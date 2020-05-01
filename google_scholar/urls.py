
from django.contrib import admin
from django.urls import path

from google_scholar.views import AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    # author
    path('author/',AuthorList.as_view(),name='author_list_url'),
    path('author/<int:pk>/',AuthorDetail.as_view(),name='author_detail_url'),
    path('author/create/',AuthorCreate.as_view(),name='author_create_url'),
    path('author/<int:pk>/update/',AuthorUpdate.as_view(),name='author_update_url'),
    path('author/<int:pk>/delete',AuthorDelete.as_view(),name='author_delete_url'),

    # article
    # list-detail-create-delete-update


    # topic
    # list-detail-create-delete-update

    # journal
    # list-detail-create-delete-update
]