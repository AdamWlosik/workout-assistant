from django import template
from django.db.models import QuerySet

register = template.Library()


@register.filter
def sort_query_set(queryset: QuerySet, field: str) -> QuerySet:
    ordered = queryset.order_by(field)
    return ordered
