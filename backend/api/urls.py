from django.urls import path, include
from . import views


urlpatterns = [
    path(
        'usuarios/', 
        include([
            # Usuários
            path('', views.UserListView.as_view(), name='list'),
            path('registrar', views.UserCreateView.as_view(), name='list'),
            path('auth/', include('djoser.urls')),
            path('auth/', include('djoser.urls.authtoken')),            
            path('deletar/<int:pk>', views.UserDestroyView.as_view(), name='delete'),
            path('editar/<int:pk>', views.UserUpdateView.as_view(), name='update'),
        ]),
        name='users'
    ),

    # Planos
    path(
        'planos/', 
        include([
            path('', views.PlanListView.as_view(), name='list'),
            path('criar', views.PlanCreateView.as_view(), name='create'),
            path('editar/<int:pk>', views.PlanUpdateView.as_view(), name='update'),
            path('deletar/<int:pk>', views.PlanDestroyView.as_view(), name='delete'),
            path('beneficios/', include([
                path('', views.PlanBenefitListView.as_view(), name='list'),
                path('criar', views.PlanBenefitCreateView.as_view(), name='create'),
                path('editar/<int:pk>', views.PlanBenefitUpdateView.as_view(), name='update'),                
                path('deletar/<int:pk>', views.PlanBenefitDestroyView.as_view(), name='delete'),
            ]), name='benefits')
        ]),
        name='plans'
    ),

    # Assinaturas
    path(
        'assinaturas/', 
        include([
            path('', views.SignatureListView.as_view(), name='list'),
            path('criar', views.SignatureCreateView.as_view(), name='create'),
            path('editar/<int:pk>', views.SignatureUpdateView.as_view(), name='update'),
            path('deletar/<int:pk>', views.SignatureDestroyView.as_view(), name='delete'),
        ]),
        name='signatures'
    ),

    # Localidades
    path(
        'localidades/', 
        include([
            path('', views.LocalityListView.as_view(), name='list'),
            path('criar', views.LocalityCreateView.as_view(), name='create'),
            path('editar/<int:pk>', views.LocalityUpdateView.as_view(), name='update'),
            path('deletar/<int:pk>', views.LocalityDestroyView.as_view(), name='update'),
        ]),
        name='localities'
    ),
    
    # Boletos
    path(
        'boletos/', 
        include([
            path('', views.TicketListView.as_view(), name='list'),
            path('criar', views.TicketCreateView.as_view(), name='create'),
            path('editar/<int:pk>', views.TicketUpdateView.as_view(), name='update'),
            path('deletar/<int:pk>', views.TicketDestroyView.as_view(), name='delete'),
        ]),
        name='tickets'
    ),
    
    # Área do cliente
    path(
        'cliente/', 
        include([
            path(
                'senha/alterar', 
                views.ChangePasswordView.as_view(),
                name='change-password'
            ),
            path(
                'assinaturas',
                views.ClientSignatureListView.as_view(),
                name='signatures'
            ),
            path(
                'boletos',
                views.ClientTicketListView.as_view(),
                name='tickets'
            ),
        ]),
        name='client'
    ),
    
    # Mensagens de suporte
    path(
        'mensagens/', 
        include([
            path('', views.MessageListView.as_view(), name='list'),
            path('criar', views.MessageCreateView.as_view(), name='create'),
            path('deletar/<int:pk>', views.MessageDestroyView.as_view(), name='update'),
        ]),
        name='localities'
    ),
]
