from django.shortcuts import render, redirect, HttpResponse
from django.template import RequestContext
from django.views.generic import View
from game.models import Stock
import datetime
# Create your views here.

class StartView( View ):
	template_name = 'start.html'

	def get(self, request):
		return render(request, self.template_name)

class CreateView( View ):

	def post(self, request):
		context = RequestContext(request)
		start_date = request.POST['start_date']
		game_type = request.POST['game_type']
		if game_type == 'weekly':
			start = datetime.datetime.strptime(start_date,"%Y-%m-%d")
			time = datetime.timedelta(days=28)
			end = start + time
			print(end)
			stocks = Stock.objects.filter(date__range=[start, end])
			print(stocks)
		return HttpResponse("yes")