from django.contrib import admin , auth
from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('artyprod/', include('artyprod.urls')),
    path('blog/',include('artyprod_blog.urls')),
   
    

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

