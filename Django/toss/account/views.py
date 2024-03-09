from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from core.models import User
from core.permissions import IsOwnerOrStaff

from .models import Account
from .serializers import AccountSerializer
from .permissions import IsOwner

class AccountListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountSignupView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializer
    
    def post(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        return self.create(request, *args, **kwargs)

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrStaff]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    
@api_view(["POST"])
@permission_classes([IsOwner])
def transfer(request):
    try:
        from_number = request.data['from']
        to_number = request.data['to']
        amount = request.data['amount']

        from_account = Account.objects.get(user_id=request.user.id, number=from_number)
        to_account = Account.objects.get(number=to_number)
        if from_account.money < amount:
            raise Exception("Not enough money.")
        
        from_account.money -= amount
        to_account.money += amount
        from_account.save()
        to_account.save()
        
        from_serializer = AccountSerializer(from_account)
        return Response(from_serializer.data, status.HTTP_202_ACCEPTED)

    except Exception as err:
        return Response({"message": str(err)}, status.HTTP_405_METHOD_NOT_ALLOWED)