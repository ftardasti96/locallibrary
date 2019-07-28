from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language
# Register your models here.

#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(Author)
#admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Author,AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','id','status','due_back')

    fieldsets = (
        (None, {
            'fields': ('book','id','imprint')
        }),
        ('Availability',{
            'fields': ('status','due_back')
        }),
    )