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
		Portfolio.objects.create(balance = 10000, initial_balance = 10000)
		portfolio = Portfolio.objects.last()
		request.session['portfolio'] = portfolio 
		if game_type == 'weekly':
			start = str( datetime.datetime.strptime(start_date,"%Y-%m-%d") )
			request.session['round'] = 0
			request.session['start_date'] = start[0:10]
			request.session['game_type'] = game_type
			request.session.set_expiry(300)
		return redirect('/game/round/')

class RoundView( View ):
	template_name = 'round.html'

	def get(self, request):
		if request.session['round'] < 12:
			request.session['round']+=1
			if request.session['game_type'] == 'weekly':
				days = request.session['round']*7
				print('days', days)
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				print('start', start)
				time = datetime.timedelta(days=days)
				end = start + time
				print('end', end)
				search_start = end - datetime.timedelta(days=7)
				print('s_start', search_start)
				stocks = Stock.objects.filter(date__range=[search_start, end])
				return render(request, self.template_name, {'stocks':stocks})
			elif request.session['game_type'] == 'monthly':
				pass
			elif request.session['game_type'] == 'yearly':
				pass
			else:
				pass
		else:
			return render(request, 'results.html')