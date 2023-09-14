from django.db import models


class Lender(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    code = models.TextField(verbose_name="Code", max_length=3)
    upfront_com = models.FloatField(verbose_name="Upfront Commission Rate")
    trial_com = models.FloatField(verbose_name="Trial Commission Rate")
    active = models.BooleanField(verbose_name="Active", default=False)

    def __str__(self):
        return self.name
