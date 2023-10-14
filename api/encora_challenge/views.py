import requests
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

    # Get the list of common words
    response = requests.get("https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt")
    common_words = response.text.splitlines()[:100]
    
    result = CommonWordsUsedController(text, common_words)
    return Response(result)
    