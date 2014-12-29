from game.models import Stock

tickers = ['GOOGL', 'MSFT', 'FB', 'YHOO', 'ORCL', 'IBM', 'AAPL', 'BBY', 'HPQ', 'AMZN', 'GE', 'XOM', 'CVX',
 'C', 'ED', 'CL', 'WSM', 'PG', 'K', 'HSY', 'DIS', 'COH', 'ALL', 'GIS', 'KWR', 'CAG', 'KO', 'PEP', 'M', 'WHR',
  'MKC', 'NKE', 'SJM', 'WFM', 'AEO', 'RL', 'HD', 'GPS', 'UA', 'CSCO', 'BBBY', 'GM', 'F', 'BAC', 'WMT', 'COST', 'JNJ', 'MET', 'VZ', 'T']

date1 = '2000-01-'
price = 100
for ticker in tickers:
	print(ticker)
	date2 = '01'
	count = 0
	print(count, 'i before')
	while (count < 30):
		count+=1
		print(count,'i after')
		price += 20
		date2 = int(date2)+1
		print('len = ', len(str(date2)))
		if len(str(date2)) == 1:
			date2 = '0'+ str(date2)
			print('went 1',date2)
			date = date1 + date2
			Stock.objects.create(ticker = ticker, price = price, date = date)
		else:
			date2 = str(date2)
			print('went 2', date2)
			date = date1 + date2
			Stock.objects.create(ticker = ticker, price = price, date = date)
print('done')