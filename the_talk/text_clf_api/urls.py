from django.conf.urls import url
from .views import Api

app_name = 'text_clf_api'

urlpatterns = [
    url(r'^$', Api.as_view()),
]