from django.db import models
from django.urls import reverse


class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    birth_year=models.IntegerField()
    affiliation=models.CharField(max_length=200)
    country=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author_detail_url',
                       kwargs={'pk': self.pk})


    def __str__(self):
        return '%s, %s' %(self.last_name,self.first_name)
    class Meta:
        ordering=['first_name','last_name','country']
        unique_together=(('first_name','last_name','birth_year','country'))

class Topic(models.Model):
    topic_id=models.AutoField(primary_key=True)
    topic_name=models.CharField(max_length=200,unique=True)
    # article list  one-to-many
    def __str__(self):
        return '%s' %(self.topic_name)
    class Meta:
        ordering=['topic_name']

class Journal(models.Model):
    journal_id=models.AutoField(primary_key=True)
    journal_name=models.CharField(max_length=100)
    establish_year=models.IntegerField()
    topic=models.ForeignKey(Topic,related_name='journals',on_delete=models.PROTECT)
    # to-do article list   one-to-many
    def __str__(self):
        return '%s' %(self.journal_name)
    class Meta:
        ordering=['journal_name']
        unique_together=(('journal_name','establish_year'))



class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    pub_year=models.IntegerField()
    pub_url=models.IntegerField(unique=True)
    citations=models.IntegerField()
    cited_by=models.IntegerField()
    author=models.ForeignKey(Author,related_name='articles',on_delete=models.PROTECT)
    journal=models.ForeignKey(Journal,related_name='articles',on_delete=models.PROTECT)
    topic=models.ForeignKey(Topic,related_name='articles',on_delete=models.PROTECT)

    def __str__(self):
        return '%s_%s' %(self.title,self.journal)
    class Meta:
        ordering=['-pub_year']






