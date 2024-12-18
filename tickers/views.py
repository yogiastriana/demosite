from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Ticker

data = [
    {
        "Symbol": "MSFT",
        "Shortname": "Microsoft Corporation",
        "Longname": "Microsoft Corporation",
        "Sector": "Technology",
        "Industry": "Software - Infrastructure",
        "Marketcap": 3092590624768,
        "City": "Redmond",
        "State": "WA",
        "Country": "United States"
    },
    {
        "Symbol": "NVDA",
        "Shortname": "NVIDIA Corporation",
        "Longname": "NVIDIA Corporation",
        "Sector": "Technology",
        "Industry": "Semiconductors",
        "Marketcap": 3064287461376,
        "City": "Santa Clara",
        "State": "CA",
        "Country": "United States"
    },
    {
        "Symbol": "GOOG",
        "Shortname": "Alphabet Inc.",
        "Longname": "Alphabet Inc.",
        "Sector": "Communication Services",
        "Industry": "Internet Content & Information",
        "Marketcap": 2064893739008,
        "City": "Mountain View",
        "State": "CA",
        "Country": "United States"
    },
    {
        "Symbol": "GOOGL",
        "Shortname": "Alphabet Inc.",
        "Longname": "Alphabet Inc.",
        "Sector": "Communication Services",
        "Industry": "Internet Content & Information",
        "Marketcap": 2064878272512,
        "City": "Mountain View",
        "State": "CA",
        "Country": "United States"
    },
    {
        "Symbol": "AMZN",
        "Shortname": "Amazon.com, Inc.",
        "Longname": "Amazon.com, Inc.",
        "Sector": "Consumer Cyclical",
        "Industry": "Internet Retail",
        "Marketcap": 1957534236672,
        "City": "Seattle",
        "State": "WA",
        "Country": "United States"
    },
    {
        "Symbol": "META",
        "Shortname": "Meta Platforms, Inc.",
        "Longname": "Meta Platforms, Inc.",
        "Sector": "Communication Services",
        "Industry": "Internet Content & Information",
        "Marketcap": 1507620814848,
        "City": "Menlo Park",
        "State": "CA",
        "Country": "United States"
    }
]

# Create your views here.
@login_required(login_url='/login/')
def tickers_view(request):

    # for record in data:
    #     Ticker.objects.create(
    #         symbol=record["Symbol"],
    #         shortname=record["Shortname"],
    #         longname=record["Longname"],
    #         sector=record["Sector"],
    #         industry=record["Industry"],
    #         marketcap=record["Marketcap"],
    #         city=record["City"],
    #         state=record["State"],
    #         country=record["Country"]
    #     )

    tickers = Ticker.objects.all()

    context = {
        'tickers': tickers
    }

    return render(request, 'tickers/tickers.html', context)


@login_required(login_url='/login/')
def save_ticker_view(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        shortname = request.POST.get('shortname')
        longname = request.POST.get('longname')
        sector = request.POST.get('sector')
        industry = request.POST.get('industry')
        marketcap = request.POST.get('marketcap')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        longbusinesssummary = request.POST.get('longbusinesssummary')

        # Create and save a new Ticker instance
        new_ticker = Ticker(
            symbol=symbol,
            shortname=shortname,
            longname=longname,
            sector=sector,
            industry=industry,
            marketcap=marketcap,
            city=city,
            state=state,
            country=country,
            longbusinesssummary=longbusinesssummary
        )
        new_ticker.save()

        tickers = Ticker.objects.all() 
        
        return render(request, 'template-parts/ticker-list.html', {'tickers': tickers})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url='/login/')
def delete_ticker_view(request):
    ticker_id = request.POST.get('ticker_id')
    ticker = Ticker.objects.get(id=ticker_id)
    ticker.delete()
    
    tickers = Ticker.objects.all()  
    
    return render(request, 'template-parts/ticker-list.html', {'tickers': tickers})  