from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model
from .models import Message, Plan, Signature, Locality, Ticket, PlanBenefit
from djoser.serializers import UserCreateSerializer

user_model = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = user_model
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'date_joined', 'last_login', 'is_manager')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['id', 'username', 'password', 'email', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['username', 'password', 'email', 'is_active']
        extra_kwargs = {
            'password': {'required': False},
            'username': {'required': False}
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)
            instance.save()

        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PlanBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanBenefit
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class ListPlanSerializer(serializers.ModelSerializer):
    benefits = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = '__all__'

    def get_benefits(self, obj):
        benefit_ids = obj.benefits.all()
        benefit_details = PlanBenefit.objects.filter(id__in=benefit_ids)
        serializer = PlanBenefitSerializer(benefit_details, many=True)
        return serializer.data


class ClientSignatureSerializer(serializers.ModelSerializer):
    plan = serializers.SerializerMethodField()

    class Meta:
        model = Signature
        fields = ['plan', 'contract', 'is_active']

    def get_plan(self, obj):
        serializer = PlanSerializer(obj.plan)
        return serializer.data


class SignatureSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()

    class Meta:
        model = Signature
        fields = '__all__'

    def get_user(self, obj):
        serializer = UserSerializer(obj.user)
        return serializer.data

    def get_plan(self, obj):
        serializer = PlanSerializer(obj.plan)
        return serializer.data


class CreateSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ['user', 'plan', 'contract']


class UpdateSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ['is_active']


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = '__all__'


class ClientTicketSerializer(serializers.ModelSerializer):
    signature = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = [
            'signature', 'expire_date', 'document', 'status', 'created_date'
        ]

    def get_signature(self, obj):
        serializer = ClientSignatureSerializer(obj.signature)
        return serializer.data


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class ListTicketSerializer(serializers.ModelSerializer):
    signature = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'

    def get_signature(self, obj):
        serializer = SignatureSerializer(obj.signature)
        return serializer.data


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

