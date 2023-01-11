from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name="home"),
    path('fake/',views.fake,name="fake"),
     path('face/',views.face,name="face"),
     path('about/',views.about,name="about"),
     path('contact/',views.contact,name="contact"),

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
