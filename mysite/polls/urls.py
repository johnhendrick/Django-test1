from django.urls import path

from . import views

# adding namespaces to URLconf. Important especially when multiple apps are expected
app_name = "polls"

# urlpatterns = [
#     path('', views.index, name='index'),  # ex: /polls/
#     # ex: /polls/5/
#     # note the 'name' value 'detail' is called by {% url %} template
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
# Generic views version:
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'), ]


# http://localhost:8000/polls/
