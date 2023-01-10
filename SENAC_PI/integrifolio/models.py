from django.db import models

# Create your models here.

class TipoCurso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self) -> str:
        return self.nome

class CURSO(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True, null=False)
    carga_horaria = models.IntegerField()
    tipo_curso = models.ForeignKey(TipoCurso, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nome

class TURMA(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome_turma = models.CharField('Nome da turma',max_length=255)
    numero_turma = models.IntegerField('Numero da turma')
    curso = models.ForeignKey(CURSO, on_delete=models.CASCADE)
    data_inicio = models.DateField('Data de Inicio')
    data_termino = models.DateField('Data de termino')
    nome_professor = models.CharField('Nome do Professor', max_length=255, )
    registro_alunos = models.CharField('Alunos', max_length=500)

    def __str__(self) -> str:
        return self.nome_turma

class EIXO(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self) -> str:
        return self.nome

class PROJETO(models.Model):
    id_turma = models.ForeignKey(TURMA, on_delete=models.CASCADE)
    nome_projeto = models.CharField('Nome do projeto', max_length=50, unique=True)
    data_inicio = models.DateField('Data de inicio')
    data_entrega = models.DateField('Data de entrega')
    observacao = models.TextField('Observação', max_length=500)
    texto = models.FileField('Texto')
    slide = models.FileField('Slide')
    video = models.FileField('Video')
    foto = models.ImageField('Foto')
    foto_capa = models.ImageField('Foto de capa')
    descricao = models.TextField('Descrição')
    eixo = models.ForeignKey(EIXO, on_delete=models.CASCADE, related_name='Projeto')
    
    DESTAQUE_CHOICE=(
        ("F", "Falso"),
        ("v", "Verdeiro"),
    )

    destaque = models.CharField(max_length=2, choices=DESTAQUE_CHOICE)

    def __str__(self) -> str:
        return self.nome_projeto

    