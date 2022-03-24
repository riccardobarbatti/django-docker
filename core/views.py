from rest_framework.response import Response
from rest_framework.views import APIView

# View User
class RegisterAPIView(APIView):
    def post(self, request):
        return Response('Hello Django 4')
