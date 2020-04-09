from instapy import InstaPy
from time import sleep

session = InstaPy(username="sacman08", password="Bsd54rel!")
session.login()
sleep(60)
session.like_by_tags(["pypi", "python3"], amount=5)
session.set_dont_like(["naked", "nsfw", "islam", "hindu", "zen", "snake"])
session.set_do_like(enabled=True, percentage=70)
session.set_do_follow(True, percentage=50, times=2)
session.set_smart_hashtags(['python3', 'programmer', 'webdeveloper'], limit=3, sort='top', log_tags=True)
session.set_ignore_if_contains(['snake', 'naked', 'nsfw'])
session.like_by_tags(amount=10, use_smart_hashtags=True)
session.like_by_locations(['212947533'], amount=5, skip_top_posts=False)
session.set_do_comment(True, percentage=50)
session.comment_by_locations(['212947533/atlanta-georgia/'], amount=100)
session.set_comments(["Nice :thumbsup:", "I like how you did that!"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.end()
