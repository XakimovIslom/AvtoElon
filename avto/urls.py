from django.urls import path

from avto import views

urlpatterns = [
    path("main/", views.MainPostListAPIView.as_view()),
    path("main/<int:pk>/", views.MainPostRetrieveAPIView.as_view()),
    path("main/similar", views.MainPostRetrieveSimilarListAPIView.as_view()),
    path("post-sub/", views.PostSubListAPIView.as_view()),
    path("district/", views.DistrictListAPIView.as_view()),
    path("filter/", views.FilterPostListAPIView.as_view()),
]
