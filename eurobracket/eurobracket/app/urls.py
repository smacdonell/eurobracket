from django.urls import path, include

from eurobracket.app.views.account.home import HomeView
from eurobracket.app.views.account.leaderboard import LeaderboardView
from eurobracket.app.views.account.make_picks import MakePicksView
from eurobracket.app.views.index import IndexView
from eurobracket.app.views.account.logout import LogoutView
from eurobracket.app.views.predictions.user import UserPredictionsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/makepicks/', MakePicksView.as_view(), name='make_picks'),
    path('account/home/', HomeView.as_view(), name='home'),
    path('account/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('predictions/<id>/', UserPredictionsView.as_view(), name='user_predictions'),
]
