from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('allcvs', views.all_cvs, name='all-cvs'),
    path('cvpr/<int:year>', views.cvpr_by_year, name='cvpr-by-year'),
    path('othercvs/<str:conf>/<int:year>', views.other_cvs, name='other-cvs'),
    path('search-retry/return=<path:return_url>', views.search_retry, name='search-retry'),
]
