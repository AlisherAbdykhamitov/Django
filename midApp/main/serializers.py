from main.models import Book, Journal
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('num_pages', 'genre')

    def create(self,validate_date):
        validate_date['name'] =self.context['request'].user
        book =Book.objects.create(validate_date)
        book.save()
        return book


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        field = ['type', 'Publisher']

