import logging
import random
from django.http import HttpResponse
from testapp.models import EagleTails

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='testapp.log', filemode='a', format='%(levelname)s %(message)s')


def testapp(request):
    logger.info('Used index')
    return HttpResponse('Seminar2 page')


def eagle_or_tails(request):
    logger.info('Used eagle_or_tails')
    n = request.GET.get('n', '5')
    res = random.choice(['Орёл', 'Решка'])
    res_w = EagleTails(res=res)
    res_w.save()
    data = EagleTails.statistic_eagle_or_tails(n)
    return HttpResponse(f'Последние пять значений: {data.items()}')

