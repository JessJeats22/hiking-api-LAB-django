from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# URL: /trails (ONE URL, ONE CLASS)
class TrailShowView(APIView):
    
    # INDEX ROUTE
    # The full endpoint for this route is GET /trails
    def get(self, request):
        return Response({ 'detail': 'HIT TRAIL INDEX ROUTE' })
