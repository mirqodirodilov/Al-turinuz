from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
		path('',indexpageview,name='index'),
		path('about/',aboutpageview,name='about'),
		path('achievements/',achievementspageview,name='achievements'),
		path('contact/',contactpageview,name='contact'),
		path('events_detail/<str:events_id>/',events_detailView,name='events-detail'),
		path('events_detaile/<str:event_id>/',events_detailepageview,name='events-detaile'),
		path('news_detail/<str:news_id>/',news_detailView,name='news-detail'),
		path('events/',eventspageview,name='events'),
		path('gallery/',gallerypageview,name='gallery'),
		path('lesson_table/',lesson_tablepageview,name='lesson-table'),
		path('mugs/',mugspageview,name='mugs'),	
		path('news/',newspageview,name='news'),
		path('news_detaile/<str:newsd_id>/',news_detailepageview,name='news-detaile'),
		path('personal/',personalpageview,name='personal'),
		path('question/',questionpageview,name='question'),
		path('reception/',receptionpageview,name='reception'),
		path('results_reception/',results_receptionpageview,name='results-reception'),
		path('results/',resultspageview,name='results'),
		path('lesson_table_detail/<int:pk>/',Lesson_table_detailview.as_view(),name='lesson-table-detail'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)