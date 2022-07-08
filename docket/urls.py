from django.contrib import admin
from django.urls import path,include
from docket_app import views as docket_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',docket_app_views.index,name="index"),
    path('todolist/', include("docket_app.urls")),
    path('account/', include("user_app.urls")),
]
