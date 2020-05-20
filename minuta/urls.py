from django.urls import path

from .views import MinutaDetail, MinutaList, MinutaCreate, MinutaDelete, MinutaUpdate

urlpatterns = [
    path('minutas/<int:pk>/', MinutaDetail.as_view(), name='minuta-detail'),
    path('minutas/<int:pk>/delete', MinutaDelete.as_view(), name='minuta-delete'),
    path('minutas/<int:pk>/edit', MinutaUpdate.as_view(), name='minuta-edit'),
    path('minutas/', MinutaList.as_view(), name='minuta-list'),
    path('minutas/add', MinutaCreate.as_view(), name='minuta-create'),

]