from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

class Test(APIView):
	
	authentication_classes = (authentication.TokenAuthentication, )
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, format=None):
		return Response({"message": "Hello"})