from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    A ViewSet providing full CRUD for transactions.

    list:   GET  /transactions/
    create: POST /transactions/
    retrieve: GET /transactions/{id}/
    update: PUT  /transactions/{id}/
    partial_update: PATCH /transactions/{id}/
    destroy: DELETE /transactions/{id}/
    summary: GET /transactions/summary/
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['transaction_type', 'category', 'date']
    search_fields = ['title', 'description', 'category']
    ordering_fields = ['date', 'amount', 'created_at']
    ordering = ['-date']

    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Returns total income, total expense and balance."""
        from django.db.models import Sum
        totals = Transaction.objects.values('transaction_type').annotate(total=Sum('amount'))
        income = next((t['total'] for t in totals if t['transaction_type'] == 'income'), 0)
        expense = next((t['total'] for t in totals if t['transaction_type'] == 'expense'), 0)
        return Response({
            'total_income': income,
            'total_expense': expense,
            'balance': (income or 0) - (expense or 0),
        })
