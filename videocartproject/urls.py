from django.contrib import admin
from django.urls import path
from main import views as m_views
from search import views as s_views 


urlpatterns = [
    path('admin/', admin.site.urls),
    #Main app urls
    path('',m_views.main_page,name='index'),
    path('item/<title>/',m_views.item_detail,name='videocart_detail'),
    #Search app urls
    path('search',s_views.search,name='search'),
]
