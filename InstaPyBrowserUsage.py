from instapy import InstaPy

session = InstaPy(username="sacman08", password="Bsd54rel!")
session.login()
session.like_by_tags(["bible","Jesus"], amount=5)
session.set_dont_like(["naked", "nsfw", "islam", "hindu", "zen", "satanic"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Thanks for this today!", "Have a blessed week!"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.end()
