from django.db import models
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

# class Menuoftheday(models.Model):

#     menuitem = models.ForeignKey('Menuitem',
#                                  on_delete=models.CASCADE,
#                                  blank=True,
#                                  null=True)

#     mealtype = models.ForeignKey('Mealtype',
#                                  on_delete=models.CASCADE,
#                                  blank=True,
#                                  null=True)

#     DAYS_OF_WEEK = (
#         (1, 'Monday'),
#         (2, 'Tuesday'),
#         (3, 'Wednesday'),
#         (4, 'Thursday'),
#         (5, 'Friday'),
#         (6, 'Saturday'),
#         (7, 'Sunday'),
#     )

#     #enum

#     days = models.IntegerField(choices=DAYS_OF_WEEK, blank=True, null=True)

#     #positive

#     def __str__(self):

#         return ' {}'.format(self.get_days_display())

# class Menuitem(models.Model):
#     name = models.CharField(_('Food item name'), max_length=30, blank=True)

#     def __str__(self):

#         return 'MyModel: {}'.format(self.name)

# class Mealtype(models.Model):

#     MEAL_CHOICE = (
#         ('B', 'breakfast'),
#         ('L', 'Lunch'),
#         ('D', 'Dinner'),
#         ('B+L', 'Breakfast&Lunch'),
#         ('B+L+D', 'Breakfast&Lunch&Dinner'),
#     )

#     PRICE_PLAN = (
#         ('M', 'MONTHLY'),
#         ('W', 'WEEKLY'),
#         ('D', 'ONE TIME'),
#     )

#     meal_type = models.CharField(_('MEAL_CHOICE'),
#                                  choices=MEAL_CHOICE,
#                                  max_length=20,
#                                  blank=True,
#                                  null=True)

#     price_plan = models.CharField(_('PRICE_PLAN'),
#                                   choices=PRICE_PLAN,
#                                   max_length=20,
#                                   blank=True,
#                                   null=True)
#     price = models.IntegerField()

#     mealschedule = models.TimeField(blank=True, default=now)

#     def __str__(self):

#         return 'Mealtype: {}'.format(self.meal_type)


class Orders(models.Model):

    pass
