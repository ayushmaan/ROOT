from django.contrib import admin
from .models import Books



class BookAdmin(admin.ModelAdmin):
    fields = ['BookName','Author','Pages','NoOfReader']
    list_display =  ['BookName','Author','Pages','NoOfReader','WhoUpdated']
    list_display_links = ['BookName','Author','Pages','NoOfReader','WhoUpdated']

admin.site.register(Books,BookAdmin)
# Register your models here.
