from rest_framework.response import Response
from rest_framework.views import APIView

class WhitelistView(APIView):
    """
    This is a test view for the whitelist API.
    """
    def get(self, request):
        data = request.query_params
        if 'address' in data:
            address = data['address']
            if address in ['0x0000000000000000000000000000000000000000', '0x0000000000000000000000000000000000000001']:
                return Response({'status': 'ok'})
            else:
                return Response({'status': 'error'})
        else:
            return Response({'status': 'error'})
