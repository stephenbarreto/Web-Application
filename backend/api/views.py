from rest_framework import status
from rest_framework.generics import (
    DestroyAPIView, ListAPIView, UpdateAPIView,
    ListCreateAPIView, CreateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    ChangePasswordSerializer, ClientSignatureSerializer, ListPlanSerializer,
    MessageSerializer, PlanSerializer, SignatureSerializer, LocalitySerializer,
    UpdateUserSerializer, UserSerializer, TicketSerializer, PlanBenefitSerializer, 
    CreateSignatureSerializer
)
from .models import Message, Signature, User, Locality, Plan, Ticket, PlanBenefit
from .permissions import IsManager
from rest_framework.parsers import MultiPartParser, FormParser


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username')
        
        if username:
            queryset = queryset.filter(username__icontains=username)
        
        return queryset


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.validated_data.get('old_password', None)
            if not user.check_password(old_password):
                return Response({"detail": "Senha atual incorreta."}, status=status.HTTP_400_BAD_REQUEST)

            # Set new password
            new_password = serializer.validated_data.get('new_password', None)
            user.set_password(new_password)
            user.save()

            return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsManager]
    serializer_class = UpdateUserSerializer


class PlanCreateView(CreateAPIView):
    serializer_class = PlanSerializer
    permission_classes = [IsManager]


class PlanListView(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = ListPlanSerializer


class PlanUpdateView(UpdateAPIView):
    queryset = Plan.objects.all()
    permission_classes = [IsManager]
    serializer_class = PlanSerializer


class PlanDestroyView(DestroyAPIView):
    queryset = Plan.objects.all()
    permission_classes = [IsManager]
    serializer_class = PlanSerializer


class SignatureCreateView(CreateAPIView):
    serializer_class = CreateSignatureSerializer
    permission_classes = [IsManager]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request, *args, **kwargs)

class SignatureListView(ListAPIView):
    queryset = Signature.objects.all()
    permission_classes = [IsManager]
    serializer_class = SignatureSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username')
        
        if username:
            queryset = queryset.filter(user__username__icontains=username)
        
        return queryset


class ClientSignatureListView(ListAPIView):
    permission_classes = [IsManager]
    serializer_class = ClientSignatureSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Signature.objects.filter(user=user)        
        return queryset


class SignatureUpdateView(UpdateAPIView):
    queryset = Signature.objects.all()
    permission_classes = [IsManager]
    serializer_class = SignatureSerializer


class SignatureDestroyView(DestroyAPIView):
    queryset = Signature.objects.all()
    permission_classes = [IsManager]
    serializer_class = SignatureSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class LocalityCreateView(CreateAPIView):
    serializer_class = LocalitySerializer
    permission_classes = [IsManager]
    

class LocalityListView(ListAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


class LocalityUpdateView(UpdateAPIView):
    queryset = Locality.objects.all()
    permission_classes = [IsManager]
    serializer_class = LocalitySerializer


class LocalityDestroyView(DestroyAPIView):
    queryset = Locality.objects.all()
    permission_classes = [IsManager]
    serializer_class = LocalitySerializer


class ClientTicketListView(ListAPIView):
    permission_classes = [IsManager]
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(signature__user=user)        
        return queryset


class TicketCreateView(CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsManager]


class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketUpdateView(UpdateAPIView):
    queryset = Ticket.objects.all()
    permission_classes = [IsManager]
    serializer_class = TicketSerializer


class TicketDestroyView(DestroyAPIView):
    queryset = Ticket.objects.all()
    permission_classes = [IsManager]
    serializer_class = TicketSerializer


class PlanBenefitCreateView(CreateAPIView):
    serializer_class = PlanBenefitSerializer
    permission_classes = [IsManager]


class PlanBenefitListView(ListAPIView):
    queryset = PlanBenefit.objects.all()
    serializer_class = PlanBenefitSerializer


class PlanBenefitUpdateView(UpdateAPIView):
    queryset = PlanBenefit.objects.all()
    permission_classes = [IsManager]
    serializer_class = PlanBenefitSerializer


class PlanBenefitDestroyView(DestroyAPIView):
    queryset = PlanBenefit.objects.all()
    permission_classes = [IsManager]
    serializer_class = PlanBenefitSerializer


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsManager]
    serializer_class = MessageSerializer


class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer


class MessageDestroyView(DestroyAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsManager]
    serializer_class = MessageSerializer

    def perform_destroy(self, instance):
        instance.is_readed = True
        instance.save()

