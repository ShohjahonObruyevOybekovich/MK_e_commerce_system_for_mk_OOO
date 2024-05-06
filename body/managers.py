from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class FlexiblePagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if 'page' in request.query_params:
            return super().paginate_queryset(queryset, request, view)
        else:
            limit_offset_pagination = LimitOffsetPagination()
            return limit_offset_pagination.paginate_queryset(queryset, request, view)
