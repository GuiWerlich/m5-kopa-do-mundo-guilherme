from rest_framework.views import APIView, Request, Response
from utils import data_processing
from exceptions import InvalidYearCupError, ImpossibleTitlesError, NegativeTitlesError
from .models import Team
from django.forms.models import model_to_dict



class TeamView(APIView):

    def post(self, request):
        team_data = request.data
        
        try:
            data_processing(team_data)
        except (InvalidYearCupError, ImpossibleTitlesError, NegativeTitlesError) as e:
            return Response({"error": str(e)}, status=400)
        
        try:
            team = Team.objects.create(**team_data)
            return Response(model_to_dict(team), status=201)
        except Exception as e:
            return Response(str(e), status=400)
            

    def get(self, request, team_id=None):

        if not team_id == None:
            found_team = Team.objects.filter(id=team_id)

            if not found_team.exists():
                return Response({"error": "Team not found"}, 404)
            
            team = Team.objects.get(id=team_id)
            return Response(model_to_dict(team))        
        
        teams = Team.objects.all()

        teams_dict = []
        
        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)

        return Response(teams_dict, 200)
    

    def delete(self, request, team_id):

        found_team = Team.objects.filter(id=team_id)

        if not found_team.exists():
            return Response({"error": "Team not found"}, 404)
        
        team = Team.objects.get(id=team_id)
        team.delete()
        return Response({"message": "Team deleted"}, 204)
    

    def patch(self, request, team_id):

        found_team = Team.objects.filter(id=team_id)

        if not found_team.exists():
            return Response({"error": "Team not found"}, 404)
        
        team = Team.objects.get(id=team_id)
        
        team.name = request.data["name"]
        team.titles = request.data["titles"]
        team.top_scorer = request.data["top_scorer"]
        team.fifa_code = request.data["fifa_code"]
        team.first_cup = request.data["first_cup"]

        team.save()

        return Response(model_to_dict(team), 200)




