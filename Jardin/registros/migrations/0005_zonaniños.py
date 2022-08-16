# Generated by Django 4.0.5 on 2022-07-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_alter_contacto_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonaNiños',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('enlace', models.TextField(verbose_name='link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Subido')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Zona de Niños',
                'verbose_name_plural': 'Zona de Niños',
                'ordering': ['created'],
            },
        ),
    ]
