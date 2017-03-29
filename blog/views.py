from django.shortcuts import render
from django.conf import settings
import logging


logger = logging.getLogger('blog.views')


# Create your views here.

# add to context_processors
def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
             'SITE_DESC': settings.SITE_DES,
             'WEIBO_SINA': settings.WEIBO_SINA,
             'WEIBO_TENCENT': settings.WEIBO_TENCENT,
             'PRO_RSS': settings.PRO_RSS,
             'PRO_EMAIL': settings.PRO_EMAIL}


def index(request):
    try:
        f = open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())
