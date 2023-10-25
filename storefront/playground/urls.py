from django.urls import path
from . import veiws

urlpatterns = [
    path('playground/hello', veiws.say_hello)
]