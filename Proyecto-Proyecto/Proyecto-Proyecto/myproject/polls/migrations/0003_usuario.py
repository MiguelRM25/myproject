# Generated by Django 5.0.4 on 2024-06-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
    ]