# Generated by Django 5.1.3 on 2024-11-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_imagem_alter_produto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.PositiveIntegerField(),
        ),
    ]
