from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, PatientViewSet, DoctorViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()

router.register('patients', PatientViewSet, basename='patient')
router.register('doctors', DoctorViewSet, basename='doctor')
router.register('mapping', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls)),
]

