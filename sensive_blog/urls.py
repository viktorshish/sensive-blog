from django.contrib import admin
from blog import views
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/<int:page>', views.get_page_index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_title>', views.get_tag_filter, name='tag_filter'),
    path('contacts/', views.get_contacts, name='contacts'),
    path('', views.get_page_index, name='index'),
    path("__debug__/", include("debug_toolbar.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
