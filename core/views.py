from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Unidade, Sala, Status, Bem, Categoria
from .serializers import (
    UnidadeSerializer,
    SalaSerializer,
    StatusSerializer,
    BemSerializer,
    CategoriaSerializer,
)

from .permissions import IsAdmin, IsProfessor, IsTecnico

@api_view(["POST"])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse({"detail": "Credenciais inválidas"}, status=401)

    login(request, user)
    return JsonResponse({"detail": "Login realizado com sucesso"})
@extend_schema(
    tags=["Unidade"],
    summary="Lista e cria Unidade",
)
class UnidadeViewSet(ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsTecnico)()]
@extend_schema(
    tags=["Sala"],
    summary="Lista e cria Sala",
)
class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsTecnico)()]
@extend_schema(
    tags=["Status"],
    summary="Lista e cria Status",
)
class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsTecnico)()]
@extend_schema(
    tags=["Categoria"],
    summary="Lista e cria Categoria",
)
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsTecnico)()]
@extend_schema(
    tags=["Bens"],
    summary="Lista e cria bens",
)
class BemListCreateView(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsProfessor | IsTecnico)()]


class BemViewSet(ModelViewSet):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsProfessor | IsTecnico)()]
class BemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), (IsAdmin | IsTecnico)()]
