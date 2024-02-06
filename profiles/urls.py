from django.urls import path, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register("profiles", api.ProfileViewSet)  # استخدم الجمع "profiles" بدلاً من "Profile"

urlpatterns = [
    path("api/v1/", include(router.urls)),  # مسارات API
    path("", views.ProfileListView.as_view(), name="profiles_list"),  # تغيير "profiles_Profile_list" إلى "profiles_list"
    path("create/", views.ProfileCreateView.as_view(), name="profiles_create"),  # تغيير "profiles_Profile_create" إلى "profiles_create"
    path("detail/<int:pk>/", views.ProfileDetailView.as_view(), name="profiles_detail"),  # تغيير "profiles_Profile_detail" إلى "profiles_detail"
    path("update/<int:pk>/", views.ProfileUpdateView.as_view(), name="profiles_update"),  # تغيير "profiles_Profile_update" إلى "profiles_update"
    path("delete/<int:pk>/", views.ProfileDeleteView.as_view(), name="profiles_delete"),  # تغيير "profiles_Profile_delete" إلى "profiles_delete"
]
