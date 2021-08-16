from django.urls import path

from . import views

urlpatterns = [
    path('allwks', views.StudentWeeks.as_view(), name="allwks"),
    path('allwks/<int:pk>', views.WeekUpdateView.as_view(), name="editwk"),
]