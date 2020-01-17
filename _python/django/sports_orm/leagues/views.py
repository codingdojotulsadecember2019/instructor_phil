from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	print('!'*70)
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		# ...all baseball leagues
		# 'leagues': League.objects.filter(sport__icontains = 'baseball')
		# ...all womens' leagues
		# 'leagues': League.objects.filter(name__icontains = 'women')
		# ...all leagues where sport is any type of hockey
		# ...all leagues where sport is something OTHER THAN football
		# ...all leagues that call themselves "conferences"
		# ...all leagues in the Atlantic region
		# ...all teams based in Dallas
		# 'teams': Team.objects.filter(location__icontains = 'dallas')
		# ...all teams named the Raptors
		# ...all teams whose location includes "City"
		# ...all teams whose names begin with "T"
		# ...all teams, ordered alphabetically by location
		# 'teams': Team.objects.all().order_by('location')
		# ...all teams, ordered by team name in reverse alphabetical order
		# 'teams': Team.objects.all().order_by('-location')
		# ...every player with last name "Cooper"
		# ...every player with first name "Joshua"
		# ...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		# ...all players with first name "Alexander" OR first name "Wyatt"

		# ...all teams in the Atlantic Soccer Conference
		'teams': Team.objects.filter(league__name__icontains = 'Atlantic Soccer Conference')
		# ...all (current) players on the Boston Penguins
		# ...all (current) players in the International Collegiate Baseball Conference
		# ...all (current) players in the American Conference of Amateur Football with last name "Lopez"
		# ...all football players
		# ...all teams with a (current) player named "Sophia"
		# ...all leagues with a (current) player named "Sophia"
		# ...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
		# ...all teams, past and present, that Samuel Evans has played with
		# ...all players, past and present, with the Manitoba Tiger-Cats
		# ...all players who were formerly (but aren't currently) with the Wichita Vikings
		# ...every team that Jacob Gray played for before he joined the Oregon Colts
		# ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		# ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
		# ...all players and count of teams played for, sorted by the number of teams they've played for
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	print('^'*70)
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")