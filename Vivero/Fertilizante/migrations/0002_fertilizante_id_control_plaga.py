# Generated by Django 4.2.1 on 2023-05-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0002_control_id_labor_control_plaga_id_control'),
        ('Fertilizante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizante',
            name='id_control_plaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control.control_plaga'),
        ),
    ]