from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from teams.models import Team
from django.forms.models import model_to_dict

class TeamsView(APIView):
    def get(self, request: Request) -> Response:

        teams = Team.objects.all()
        # teams_list = []

        # for team in teams:
        #     team_dict = model_to_dict(team)
        #     teams_list.append(team_dict)

        teams_list = [model_to_dict(team) for team in teams]

        return Response(teams_list, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        new_team = model_to_dict(Team.objects.create(**request.data))

        return Response(new_team, status=status.HTTP_201_CREATED)
    
class TeamsDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = model_to_dict(Team.objects.get(id=team_id))
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)
       
        return Response(team, status=status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response :
        try:
            team =Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)

        # team.name = request.data.get('name', team.name)
        # team.titles = request.data.get('titles', team.titles)
        # team.top_score = request.data.get('top_score', team.top_score)
        # team.fifa_code = request.data.get('fifa_code', team.fifa_code)
        # team.founded_at = request.data.get('founded_at', team.founded_at)

        for key, value in request.data.items():

            setattr(team, key, value)
            
        team.save()

        return Response(model_to_dict(team), status=status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)
        
        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

