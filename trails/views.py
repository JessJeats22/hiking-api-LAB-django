from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trail

# Create your views here.

# URL: /trails (ONE URL, ONE CLASS)
class TrailShowView(APIView):
    
    # INDEX ROUTE
    # The full endpoint for this route is GET /trails
    def get(self, request):
        trails = Trail.ojects.all()
        print (trails)
        return Response({ 'detail': 'HIT TRAIL INDEX ROUTE' })
