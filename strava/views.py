from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from stravaio import strava_oauth2
from stravaio import StravaIO

MY_STRAVA_CLIENT_ID = '44247'
MY_STRAVA_CLIENT_SECRET = '7224bbf5323a86ee18e2fafb5fe084d52991474c'

# Create your views here.
def home(request):
	return render(request, 'strava/athlete_info.html', {'file_name':'strava/heatmap_data/Athelete_'+str(1)+'.html', 'id':1})

def stravaAuthentication(request):
	print('check')
	auth_res = strava_oauth2(client_id=MY_STRAVA_CLIENT_ID, client_secret=MY_STRAVA_CLIENT_SECRET)
	client = StravaIO(access_token=auth_res['access_token'])
	athlete = client.get_logged_in_athlete()
	athlete = athlete.to_dict()
	print(athlete)
	return HttpResponse("Athlete Authenticated: " + athlete['firstname'])

def sampleData(request):
	return HttpResponse("In sample data ")

def athlete_info(request, ath_id):
	import pickle
	with open("strava/home_address/athlete_"+str(ath_id),'rb') as f:
		address = pickle.load(f)
		print(address)
	return render(request, 'strava/athlete_info.html', {'file_name':'strava/heatmap_data/Athelete_'+str(ath_id)+'.html', 'id':ath_id,'address':address})

def start_end(request, ath_id):

	return render(request, 'strava/start_end.html', {'file_name':"strava/startEndData/Athelete_" + str(ath_id) + ".html", 'id':ath_id})

def rest_spots(request,ath_id):
	return render(request,'strava/restspots.html',{'file_name':"strava/RestSpots_Data/athlete_"+str(ath_id)+".html",'id':ath_id})

def frequent_spots(request, ath_id):
	return render(request, 'strava/frequent_spots.html', {'file_name':"strava/FrequentSpotsData/athlete "+str(ath_id)+"frequency_and_time_plots_.html",'id':ath_id})

def avg_speed(request, ath_id):
	return render(request, 'strava/avg_speed.html', {'file_name':"strava/AvgSpeed/athlete"+str(ath_id)+"_graph.html",'id':ath_id})

def athelete_overlap(request):
	return render(request, 'strava/multiple_atheletes.html', {'file_name':'strava/athelete_overlap.html'})