from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    email = models.EmailField(
        verbose_name='Email do usuário', blank=True, unique=True
    )
    is_manager = models.BooleanField(
        verbose_name='É um administrador', default=False
    )

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username


class PlanBenefit(models.Model):
    class Meta:
        verbose_name = 'Benefício do plano'
        verbose_name_plural = 'Benefícios do plano' 

    name = models.CharField(verbose_name='Nome do benefício', max_length=100)
    description = models.TextField(verbose_name='Descrição do benefício', null=True, blank=True)


class Plan(models.Model):
    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    name = models.CharField(verbose_name='Nome do plano', max_length=100)
    value = models.DecimalField(
        verbose_name='Valor do plano', default=0, decimal_places=2, max_digits=6
    )
    benefits = models.ManyToManyField(
        PlanBenefit, verbose_name='Benefícios do plano', blank=True
    )


class Locality(models.Model):
    class Meta:
        verbose_name = 'Localidade'
        verbose_name_plural = 'Localidades'

    city = models.CharField(verbose_name='Cidade', max_length=100)
    state = models.CharField(verbose_name='Estado', max_length=100)


class Signature(models.Model):
    class Meta:
        verbose_name = 'Assinatura'
        verbose_name_plural = 'Assinaturas'

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    contract = models.FileField(verbose_name='Contrato', null=True, upload_to='contratos/')
    is_active = models.BooleanField(verbose_name='Assinatura ativa?', default=True)


class Ticket(models.Model):
    class Meta:
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'

    STATUS_CHOICES = (
        (0, 'Aguardando pagamento'),
        (1, 'Pago'),
        (2, 'Expirado')
    )
    
    signature = models.ForeignKey(Signature, on_delete=models.PROTECT)
    created_date = models.DateField(verbose_name='Data de criação', auto_now_add=True)
    updated_date = models.DateField(verbose_name='Data da última alteração', auto_now=True)
    expire_date = models.DateField(verbose_name='Data limite para o pagamento')
    status = models.IntegerField(verbose_name='Status', choices=STATUS_CHOICES, default=0)
    document = models.FileField(verbose_name='Boleto', blank=True, upload_to='boletos/')


class Message(models.Model):
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    name = models.CharField(verbose_name='Nome do cliente', max_length=250)
    email = models.EmailField(verbose_name='E-mail do cliente')
    description = models.TextField(verbose_name='Descrição da mensagem')
    is_readed = models.BooleanField(verbose_name='Foi lida?', default=False)
    created_date = models.DateField(verbose_name='Data de criação', auto_now_add=True)

