from django.urls import path
from .views import OrganizationBalanceAPIView

urlpatterns = [
    path('organizations/<str:inn>/balance/', OrganizationBalanceAPIView.as_view(), name='org-balance'),
]
