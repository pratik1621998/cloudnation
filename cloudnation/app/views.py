from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EnvironmentVariable, UserAppDetails
from .serializers import *

# Create your views here.

#--------------------------- CREATE USER CLOUD APP ----------------------#

class CreateAppApiView(APIView):
    serializer_class = UserAppSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get_user_app = UserAppDetails.objects.filter(id=serializer.data.get("id"), app_name=serializer.data.get("app_name")).first()
            environment_variable = request.data.get("environment_variables")
            for env_key, env_value in environment_variable.items():
                EnvironmentVariable.objects.create(
                    key=env_key,
                    value=env_value,
                    user_app=get_user_app,  
                )
            return Response({
                "status":"success",
                "message": "User data is saved successfully.",
                "data":serializer.data,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status":"failed",
                "message": "Something went wrong.",
                "data":serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

#--------------------------- GET USER CLOUD DATA --------------------#

class UserAppCloudDataApi(APIView):
    serializer_class = UserAppSerializer

    def get(self, request, pk):
        get_user_cloud_data = UserAppDetails.objects.filter(id=pk).first()
        get_all_env_data = EnvironmentVariable.objects.filter(user_app = get_user_cloud_data)
        env_dict = {}
        for environment_variable_value in get_all_env_data:
            name_value = environment_variable_value.key
            value_value = environment_variable_value.value

            env_dict[name_value] = value_value
            
        if get_user_cloud_data:
            serializer = self.serializer_class(get_user_cloud_data)
           
            return Response({
                    "status":"success",
                    "message": "User cloud data.",
                    "data":serializer.data,
                    "user_environment_data":env_dict
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                    "status":"failed",
                    "message": "User cloud data not found.",
                }, status=status.HTTP_404_NOT_FOUND)


#--------------------------- ENVIRONMENT VARIABLES UPDATE AND DELETE --------------------#
        
class EnvironmentVariableAPI(APIView):
    serializer_class = EnvironmentVariableSerializer

    def patch(self, request, pk):
        get_env_object = EnvironmentVariable.objects.filter(id=pk).first()
        if get_env_object:
            serializer = self.serializer_class(get_env_object,data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status":"success",
                    "message": "Environment variable updated successfully.",
                    "data":serializer.data,
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "status":"failed",
                    "message": "Something went wrong.",
                    "data":serializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                    "status":"failed",
                    "message": "Environment variable not found.",
                }, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request, pk):
        try:
            get_env_object = EnvironmentVariable.objects.filter(id=pk).first()
            get_env_object.delete()
            return Response({
                "status":"success",
                "message": "Environment variable deleted successfully.",
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "status":"failed",
                "message": "Environment variable not found.",
            }, status=status.HTTP_404_NOT_FOUND)



        










