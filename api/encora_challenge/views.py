from rest_framework.views import APIView
from rest_framework.response import Response
from encora_challenge.controllers import CommonWordsUsedController

class CommonWordsUsed(APIView):

  def get(self, request):
    return Response("Hello world!")
  
  def post(self, request):
    text = request.data.get('text', '')
    
    if not isinstance(text, str):
      text = text.read().decode('utf-8')
    
    result = CommonWordsUsedController(text)
    return Response(result)
    