# importing api
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


def index(request):
    newsapi = NewsApiClient(api_key='Your api_key on newsapi')
    ign_headlines = newsapi.get_top_headlines(
        sources='ign, bbc-news, cnn, the-washington-post, ars-technica, politico, google-news')
    title_ign, desc_ign, img_ign, url_ign, time_ign, content_ign = (
        [], [], [], [], [], [])

    articles1 = ign_headlines['articles']
    for each in range(len(articles1)):
        ign_article = articles1[each]
        title_ign.append(ign_article["title"])
        time_ign.append(ign_article["publishedAt"])
        desc_ign.append(ign_article["description"])
        img_ign.append(ign_article["urlToImage"])
        url_ign.append(ign_article["url"])
        content_ign.append(ign_article["content"])
    myignlist = zip(title_ign, desc_ign,
                    img_ign, url_ign)

    return render(request, 'newsapp/index.html', context={"myignlist": myignlist})
