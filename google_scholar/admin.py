from django.contrib import admin
from .models import Article, Author, Journal, Topic

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Journal)
admin.site.register(Topic)
