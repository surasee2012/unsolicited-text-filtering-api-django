from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('text_clf_api/', include('text_clf_api.urls'))
]
