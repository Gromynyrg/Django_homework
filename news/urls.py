from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.news_home, name='news_home'),
                  path('create/', views.create, name='create'),
                  path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
                  path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
                  path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
