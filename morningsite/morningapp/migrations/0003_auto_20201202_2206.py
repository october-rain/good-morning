# Generated by Django 3.1.3 on 2020-12-02 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morningapp', '0002_auto_20201202_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='userID',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_user', to='morningapp.userinfo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userID',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to='morningapp.userinfo'),
        ),
    ]
