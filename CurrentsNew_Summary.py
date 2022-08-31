import json

final_summary = {}
articles_file = 'currents_news.json'
fObj = open(articles_file)
our_news_raw = json.load(fObj)
for each_summary in our_news_raw['news']:
    final_summary['title'] = each_summary['title']
    final_summary['description'] = each_summary['description']
    final_summary['url'] = each_summary['url']
    print(f"{final_summary['title']} \n {final_summary['description']} \n {final_summary['url']} \n")
