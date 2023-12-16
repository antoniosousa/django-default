from django.db import models


class Projeto(models.Model):
    titulo = models.CharField(
        verbose_name="título do projeto",
        max_length=100,
        help_text="título do projeto",
    )
    descricao = models.TextField(
        verbose_name="descrição do projeto", help_text="descrição do projeto"
    )
    tecnologia = models.CharField(
        max_length=20,
        verbose_name="tecnologia usada no projeto",
        help_text="tecnologia usada no projeto",
    )
    imagem = models.FileField(
        verbose_name="Imagem do projeto",
        help_text="Imagem do projeto",
        upload_to="imagens/",
        blank=True,
    )

    class Meta:
        db_table: str = "projeto"
        verbose_name: str = "projeto"
        verbose_name_plural: str = "projetos"
