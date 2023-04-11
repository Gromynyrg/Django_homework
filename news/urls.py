from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.news_home, name='news_home'),
                  path('create/', views.create, name='create'),
                  path('<slug:slug>', views.NewsDetailView.as_view(), name='news-detail'),
                  path('<slug:slug>/update', views.NewsUpdateView.as_view(), name='news-update'),
                  path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='news-delete')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
