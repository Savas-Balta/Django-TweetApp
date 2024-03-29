from django.urls import path
from . import views


app_name = "tweetapp"

urlpatterns = [
    path("", views.listtweet, name="listtweet"),
    path("addtweet/",views.addtweet , name="addtweet"),
    path("addtweetbyform",views.addtweetbyform, name="addtweetbyform"),
    path("signup/",views.SignUpview.as_view(),name="signup"),  # buradaki as_view() class olduğu için eklenir eğer bi fonksiyon olsaydı def gibi eklenmiyecekti.
    path("deletetweet/<int:id>/",views.deletetweet,name="deletetweet"),
]