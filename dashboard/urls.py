from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path("", views.FeedView.as_view(), name="dashboard_feed"),
    path("register/post", views.register_post, name="register_post"),
    path("register/usuario", views.UsuarioFormView.as_view(), name="register_usuario"),
    path("update/usuario/<pk>", views.UsuarioUpdateView.as_view(), name="update_usuario")


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
