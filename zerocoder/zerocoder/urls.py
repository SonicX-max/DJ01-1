from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Импортируйте маршруты из вашего приложения main
    path('news/', include('news.urls'))
]