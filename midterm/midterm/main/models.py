from django.db import models
import datetime
from midterm.main import constants


class BookJournalBase(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now)



    class Meta:
        abstract = True

    def __str__(self):

        return self.name


class Book(BookJournalBase):
    num_pages =models.IntegerField()
    genre = models.CharField(max_length=40)

    class Meta:
        abstract = False


class Journal(models.Model):
    type = models.PositiveSmallIntegerField(choices=constants.JOURNAL_TYPES,default=constants.Journal_Food)
    publisher = models.CharField(max_length=40)

    class Meta:
        abstract = False

