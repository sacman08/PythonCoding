from operator import itemgetter
import requests

# Make the API call for top stories response file
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Process file for each story
submission_ids = r.json()
submission_dicts = []
for submission in submission_ids[:30]:
    # call each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission}.json'
    r = requests.get(url)
    print(f'id: {submission}\tstatus: {r.status_code}')
    response_dict = r.json()

    # Build a dict for each sub

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'https://news.ycombinator.com/item?id={submission}',
            'comments': response_dict['descendants']
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f'Problem with one article: {submission}')
        pass

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

articles_file = 'HN_TopStories_Summary.txt'
with open(articles_file, 'w') as f:
    for submission_dict in submission_dicts:
        f.write(f"\nTitle: {submission_dict['title']}\n\
                Discussion: {submission_dict['hn_link']}\n\
                Comments: {submission_dict['comments']}")
