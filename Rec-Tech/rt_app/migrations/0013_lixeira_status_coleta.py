# Generated by Django 5.0.4 on 2024-04-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rt_app', '0012_delete_aviso'),
    ]

    operations = [
        migrations.AddField(
            model_name='lixeira',
            name='status_coleta',
            field=models.BooleanField(default=False),
        ),
    ]