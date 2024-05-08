from django.urls import path
from .views import Trolley_Items

urlpatterns = [
    path('', Trolley_Items.as_view(), name="trolley_items"),

]
