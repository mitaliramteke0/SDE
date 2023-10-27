from rest_framework import generics, renderers
from .models import Expense, Balance
from .serializers import ExpenseSerializer, BalanceSerializer
from rest_framework import status
from rest_framework.response import Response
from .forms import ExpenseForm

class ExpenseCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'expense_manager/expense_create.html'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Expense created successfully'}, template_name='expense_manager/expense_create.html')
        return Response({'serializer': serializer, 'form': ExpenseForm()}, template_name='expense_manager/expense_create.html')


    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer}, template_name='expense_manager/expense_create.html')

class BalanceListCreateView(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class MyHTMLView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'expense_manager/expense_list.html'

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.all()  # You can customize this queryset as needed
        context = {
            'expenses': expenses,
        }
        return Response(context, template_name=self.template_name)
