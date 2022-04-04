from django.urls import path
from .views import *

app_name = 'university'

urlpatterns = [
    path('', UniversityViews.as_view(), name='universities'),
    path('new/<int:pk>', UniversityDetail.as_view(), name='detail-page'),
    path('update/<int:pk>', UpdateNews.as_view(), name='update'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='delete'),
    path('create/', AddViews.as_view(), name='add-page'),
    path('universities/', Universities.as_view(), name='list-universities'),
    path('mit/', Mit.as_view(), name='mit'),
    path('columbia/', Columbia.as_view(), name='columbia'),
    path('harvard/', Harvard.as_view(), name='harvard'),
    path('stanford/', Stanford.as_view(), name='stanford'),
    path('news/', AllNews.as_view(), name='news-list'),
    path('home/', HomeViews.as_view(), name='home'),
    path('education/', EducationViews.as_view(), name='education')
]