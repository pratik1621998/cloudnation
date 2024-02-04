from django.urls import path
from .views import CreateAppApiView, UserAppCloudDataApi, EnvironmentVariableAPI

urlpatterns = [
    path('create-cloud', CreateAppApiView.as_view(), name="create-user-cloud"),
    path('get-user-cloud-data/<uuid:pk>', UserAppCloudDataApi.as_view(), name="get-user-cloud-data"),

    path('user-env/<uuid:pk>', EnvironmentVariableAPI.as_view(), name="user-env"),


]