from django.contrib import admin

from main.models import Book, BookJournalBase, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'num_pages']
    ordering = ['name']

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
   list_display = [ 'publisher', 'type']
   ordering = ['name']
   search_fields = ['name', 'type']