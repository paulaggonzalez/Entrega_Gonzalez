# Generated by Django 4.1.5 on 2023-03-17 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=300)),
                ('categoriaN', models.CharField(choices=[('animales', 'Animales'), ('viajes', 'Viajes'), ('tecnologia', 'Tecnologia'), ('entrenamiento', 'Entrenamiento')], default='', max_length=20)),
                ('encabezado', models.CharField(max_length=300)),
                ('descripcion', models.TextField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('imagenNoticias', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]