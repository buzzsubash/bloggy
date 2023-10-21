from urllib import request

from django.db.models.signals import post_save
from django.dispatch import receiver
from bloggy import settings
from django.core import management
from bloggy.models import Article
from urllib.parse import urlencode

PING_GOOGLE_URL = "https://www.google.com/webmasters/tools/ping"
INDEX_NOW = "https://www.bing.com/indexnow?url={}&key={}"


@receiver(post_save, sender=Article)
def post_saved_action_signal(sender, instance, created, **kwargs):
    # Update category count everytime three is a new object added
    if created:
        print("Sendr:{}, kwargs:{}".format(sender, kwargs))
        management.call_command('update_category_count')

    if instance.publish_status == "PUBLISHED":
        if settings.PING_GOOGLE_POST_UPDATE:
            ping_google()

        if settings.PING_INDEX_NOW_POST_UPDATE:
            ping_index_now(instance)


def ping_google():
    try:
        params = urlencode({"sitemap": settings.SITE_URL + "/sitemap.xml"})
        response = request.urlopen("%s?%s" % (PING_GOOGLE_URL, params))
        if response.code == 200:
            print("Successfully pinged this page for Google!")
    except Exception:
        print("Error while pinging google")


def ping_index_now(article):
    try:
        response = request.urlopen(
            INDEX_NOW.format(article.get_absolute_url(), settings.INDEX_NOW_API_KEY))
        if response.code == 200:
            print("Successfully pinged this page for IndexNow!")
    except Exception:
        print("Error while pinging google")