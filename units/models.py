from django.db import models
from django.contrib.auth.models import User

ITEM_TYPES = (
    ("KA", "Key Activities", "КД", "Ключевые виды деятельности"),
    ("KP", "Key Partners", "КП", "Ключевые партнеры"),
    ("KR", "Key Resources", "КР", "Ключевые ресурсы"),
    ("CSt", "Cost Strusture", "СИ", "Структура издержек"),
    ("CR", "Customer Relationships", "ВК", "Взаимоотношения с клиентами"),
    ("CSg", "Customer Segments", "ПС", "Потребительский сегмент"),
    ("VP", "Value Propositions", "ЦП", "Ценностное предложение"),
    ("CH", "Channels", "КС", "Каналы сбыта"),
    ("RSt", "Revenue Streams", "ПД", "Потоки поступления доходов") 
)

def get_item_types(lang="en"):
    if lang == "ru":
        return tuple(map(lambda x: tuple(x[2:]), ITEM_TYPES))
    return tuple(map(lambda x: tuple(x[:2]), ITEM_TYPES))

class Unit(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    desc = models.TextField()
    created_at = models.ForeignKey(User)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_at = models.ForeignKey(User)
    updated_by = models.DateTimeField(auto_now=True)

class Item(models.Model):
    content = models.TextField(null=False, blank=False)
    order = models.IntegerField(default=0, null=False, blank=False)
    item_type = models.CharField(max_length=3, choices=get_item_types(), null=False, blank=False)
    unit = models.ForeignKey(Unit, null=False, blank=False)
    created_at = models.ForeignKey(User)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_at = models.ForeignKey(User)
    updated_by = models.DateTimeField(auto_now=True)


