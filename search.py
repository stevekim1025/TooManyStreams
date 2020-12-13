from justwatch import JustWatch
import pprint

def searchName(title):
    just_watch = JustWatch(country='US')
    results = just_watch.search_for_item(
        query = title,
        providers = ['nfx', 'amp', 'dnp', 'hlu', 'hbm', 'pct', 'ifd', 'cru'])
    if (not results['items']):
        print("No Results Found.")
    else:
        firstResult = results['items'][0]
        title = firstResult['title']
        pp = pprint.PrettyPrinter(indent=2)
        print(title)
        # pp.pprint(firstResult)

        wantedProviders = [8,9,15,337,384,386,238,283]
            # provider id
            # netflix: 8
            # amazon prime: 9
            # disney plus: 337
            # hulu: 15
            # hbo max: 384
            # peacock: 386
            # imdb: 238
            # cruncy roll: 283

        for offer in firstResult['offers']:
            if (offer['provider_id'] in wantedProviders):
                pp.pprint(offer)
