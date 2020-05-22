from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home-view'),
    path('stravaUser/', views.stravaAuthentication, name='strava-authentication'),
    path('sampleData/', views.sampleData, name='sample-data'),
    path('athlete/<int:ath_id>/', views.athlete_info, name='athlete_info'),
    path('athlete/<int:ath_id>/start_end', views.start_end, name='start_end'),
    path('athlete/<int:ath_id>/rest_spots', views.rest_spots, name='rest_spots'),
    path('athlete/<int:ath_id>/frequent_spots', views.frequent_spots, name='frequent_spots'),
    path('athlete/<int:ath_id>/avg_speed', views.avg_speed, name='avg_speed'),
    path('athelete_overlap/', views.athelete_overlap, name='athelete_overlap')
]