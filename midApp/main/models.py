import datetime

from django.db import models

class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)


class Journal(BookJournalBase):
    Bullet = 'Bl'
    Food = 'Fd'
    Travel = 'Tl'
    Sport = 'Sp'
    CHOICES = [
        (Bullet, 'Bullet'),
        (Food, 'Food'),
        (Travel, 'Travel'),
        (Sport, 'Sport')
    ]

    type = models.CharField(max_length=20,choices = CHOICES, default = Bullet)
    publisher = models.CharField(max_length=100)



