from django.urls import path
from . import views

urlpatterns = [
    path('get-trn-details/',views.get_trn_details),
    # path('get-responce/',views.get_responce)

]