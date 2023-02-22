from ninja import ModelSchema, NinjaAPI, Schema, UploadedFile
from .models import Livro
import json
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

api = NinjaAPI()

#LISTAR TODOS OS LIVROS
@api.get('livro/')
def listar (request):
    livro = Livro.objects.all() 
    response = [{'id': i.id, 'titulo': i.titulo, 'descricao': i.descricao, 'autor': i.autor} for i in livro]
    return response
    
#PROCURAR POR ID
@api.get('livro/{id}')
def listar_livro(request, id:int):
    livro = get_object_or_404(Livro, id=id)
    return model_to_dict(livro)

#consultar livro por padrão id=1
@api.get('livro_consulta/')
def listar_consultar(request, id:int = 1):
    livro = get_object_or_404(Livro, id=id)
    return model_to_dict(livro)
    
class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = "__all__"

#para receber e enviar varios livros
'''from typing import List
livro: List[LivroSchema]'''

#receber e enviar livro schema 1 livro schema
@api.post('livro', response=LivroSchema)                     #post nao pode ter barra no final
def livro_criar(request, livro: LivroSchema):
    l1 = livro.dict()
    livro = Livro(**l1)                                      # vai salvar todos os atributos
    livro.save()
    return livro                                             # Licro Schema já serializou
    
#receber um arquivo
@api.post('/file')
def file_upload(request, file: UploadedFile):
    print(file.size)
    return 1


