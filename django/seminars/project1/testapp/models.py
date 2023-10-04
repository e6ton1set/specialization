from django.db import models
from django.utils import timezone


class EagleTails(models.Model):
    cur_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=20)

    @staticmethod
    def statistic_eagle_or_tails(n):
        n = int(n)
        res_dict = {"Орёл": 0, "Решка": 0}
        query = list(EagleTails.objects.all())
        temp_list = query[-n:]
        for item in temp_list:
            if "Орёл" in str(item):
                res_dict["Орёл"] += 1
            elif "Решка" in str(item):
                res_dict["Решка"] += 1
        return res_dict

    def __str__(self):
        return f"time: {self.cur_time}, res: {self.res}"
