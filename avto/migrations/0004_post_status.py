# Generated by Django 5.0.2 on 2024-02-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0003_post_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('Vip', 'Vip'), ('Zor', 'Zor'), ('Alo', 'Alo')], max_length=128, null=True),
        ),
    ]
