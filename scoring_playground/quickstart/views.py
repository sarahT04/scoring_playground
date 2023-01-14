from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable, ParseError
# Self functions and constants
from .constants import *
from .utils import get_scores, get_score
from .serializers import ScoresSerializer
# For helpers
from functools import reduce
from operator import add
# Create your views here.

class PostScores(APIView):
    def post(self, request):
        try:
            if type(request.data['answer_list']) != 'list':
                raise NotAcceptable('You\'re not giving an array for answer_list.')
            scores = get_scores(request.data['real_key'], request.data['answer_list'])
            serializer = ScoresSerializer(scores, many=True)
            return Response(serializer.data)
        except:
            raise ParseError('Unexpected error happened.')

class PostScore(APIView):
    def post(self, request):
        try:
            if type(request.data['answer_list']) == 'list':
                raise NotAcceptable('You\'re not giving an array for answer_list.')
            scores = get_score(request.data['real_key'], request.data['answer_list'])
            serializer = ScoresSerializer(scores)
            return Response(serializer.data)
        except:
            raise ParseError('Unexpected error happened.')

class Main(APIView):
    def get(self, request):
        scores = [get_scores(default_key_asmat, answers_list_asmat), get_scores(default_key_cia, answers_list_cia, start=len(answers_list_asmat))]
        scores = reduce(add, scores)
        serializer = ScoresSerializer(scores, many=True)
        return Response(serializer.data)
    