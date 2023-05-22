# Generated by Django 4.2.1 on 2023-05-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fertilizante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_fertilizante', models.CharField(max_length=15)),
                ('nombre_fertilizante', models.CharField(max_length=50)),
                ('valor_fertilizante', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]