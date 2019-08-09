from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditional Django View'
        ]

        return Response({
            'message': 'Hello!',
            'view': an_apiview
        })