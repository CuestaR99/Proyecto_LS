# Generated by Django 4.2.1 on 2023-05-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Labor', '0001_initial'),
        ('Control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='control',
            name='id_labor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Labor.labor'),
        ),
        migrations.AddField(
            model_name='control_plaga',
            name='id_control',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control.control'),
        ),
    ]
