from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bloggy import models

DEFAULT_PAGE_SIZE = 20


def get_recent_feed(publish_status="LIVE", page=1, page_size=DEFAULT_PAGE_SIZE):
    articles = models.Article.objects.prefetch_related("category") \
        .filter(publish_status=publish_status) \
        .filter(post_type__in=["article", "quiz", 'lesson']) \
        .order_by("-published_date")

    paginator = Paginator(articles, page_size)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return articles


def get_recent_posts(publish_status="LIVE", page=1, page_size=DEFAULT_PAGE_SIZE):
    articles = models.Article.objects.prefetch_related("category") \
        .filter(publish_status=publish_status).filter(post_type__in=["article"]) \
        .order_by("-published_date")

    paginator = Paginator(articles, page_size)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return articles


def get_recent_quizzes(publish_status="LIVE", page=1):
    articles = models.Article.objects.prefetch_related("category") \
        .filter(publish_status=publish_status).filter(post_type__in=["quiz"]) \
        .order_by("-published_date")
    paginator = Paginator(articles, DEFAULT_PAGE_SIZE)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return articles


def get_recent_quizzes(publish_status="LIVE", page=1):
    articles = models.Article.objects.filter(publish_status=publish_status, post_type="quiz") \
        .prefetch_related("category", "quizquestion_set") \
        .order_by("-display_order")
    paginator = Paginator(articles, DEFAULT_PAGE_SIZE)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return articles


def get_quiz_by_id(pk):
    return models.Article.objects.get(pk=pk)