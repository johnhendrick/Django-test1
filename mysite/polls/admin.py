from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice)

# admin1 username&pass


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # fieldsets = [
    #     ('Question###', {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    #     # ('Choices###', {'fields': ['choice_text']})
    # ]
    # inlines = [ChoiceInLine]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
