from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_index, name='event_index'),
    path('match_detail/<int:id>', views.event_detail, name='event_detail'),
    path('search_result', views.search, name="search"),

    # les pages par categorie :
    path('ligue_1_matchs', views.ligue_1_matchs, name="ligue_1_matchs"),
    path('ligue_2_matchs', views.ligue_2_matchs, name="ligue_2_matchs"),
    path('Amateur_League_Matchs', views.amateur_league_matchs, name="amateur_league_matchs"),
    path('coupe_de_tunisie_matchs', views.coupe_de_tunisie_matchs, name="coupe_de_tunisie_matchs"),
]