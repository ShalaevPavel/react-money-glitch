from . import views
from django.urls import path

from django.conf.urls import static
from django.conf import settings

urlpatterns = [
                  path("", views.some_test, name="index"),
                #path("", views.default_map, name="а"),
                #path("", views.home, name="smth"),
               path("test/", views.index, name="test"),
               path("marks/<pk>/", views.MarksDetailView.as_view(),),
               path("some/", views.marks_create, name='void' ),
               path("try/", views.site_func, name='vs' ),



               ] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)