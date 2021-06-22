from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('author-ranking/<str:conf>/<int:year>', views.author_ranking, name='author-ranking'),
    path('paper-statistics', views.paper_statistics, name='paper-statistics'),
    path('word-cloud', TemplateView.as_view(template_name='statistics/word-cloud.html'), name='wordcloud'),
]
