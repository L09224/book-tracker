# Generated by Django 4.2.14 on 2024-08-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='status',
            field=models.CharField(choices=[('reading', 'Reading'), ('completed', 'Completed'), ('to_read', 'Plan to Read')], default='reading', max_length=20),
        ),
    ]
