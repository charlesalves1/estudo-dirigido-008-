from django .urls import path
from .views import (UnidadeListCreate,SalaListCreate,StatusListCreate,BemListCreate,BemDetail)
urlpatterns = [path ("unidades/", UnidadeListCreate.as_view()),
               path ("salas/", SalaListCreate.as_view()),
               path ("status/", StatusListCreate.as_view()),
               path ("bens/", BemListCreate.as_view()),
               path ("bens/<int:pk>/", BemDetail.as_view()),]