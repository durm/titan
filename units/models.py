from django.db import models

ITEM_TYPES = (
    ("КД", "Ключевые виды деятельности"),
    ("КП", "Ключевые партнеры"),
    ("КР", "Ключевые ресурсы"),
    ("СИ", "Структура издержек"),
    ("ВК", "Взаимоотношения с клиентами"),
    ("ПС", "Потребительский сегмент"),
    ("ЦП", "Ценностное предложение"),
    ("КС", "Каналы сбыта"),
    ("ПД", "Потоки поступления доходов") 
)

class Unit(models.Model):
    name = models.CharFeild(max_length=256, blank=False, null=False)
    desc = models.TextField()

class Item(models.Model):
    content = models.TextField(null=False, blank=False)
    order = models.IntegerField(default=0, null=False, blank=False)
    item_type = models.CharField(max_length=2, choices=ITEM_TYPES, null=False, blank=False)
    unit = models.ForeignKey(Unit, null=False, blank=False)


