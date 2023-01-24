

def skill_news(*args):

    import core.luna_core as coremodules
    import core.luna_utils as lunautils
    import requests
    import json
    import time

    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=1d7083d64d014b6e8370585ac33c82b8'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    coremodules.luna_speak('Source: The Times Of India')
    coremodules.luna_speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        coremodules.luna_speak(articles['title'])
        if index == len(arts)-1:
            break
        time.sleep(2)
    coremodules.luna_speak("That's it for today")

#     url = ('https://newsapi.org/v2/everything?'
#         'q=google&'
#         'from=2023-01-20&'
#         'sortBy=popularity&'
#         'apiKey=1d7083d64d014b6e8370585ac33c82b8')

#     response = requests.get(url)
#     newss = response.json()
#     for x in range(1,10):
#         article = newss["articles"][x]['title']

#         print(article)

# get_news()