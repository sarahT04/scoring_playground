from rest_framework import serializers

class ScoresSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   id = serializers.IntegerField()
   key = serializers.CharField()
   answer = serializers.CharField()
   score = serializers.IntegerField()