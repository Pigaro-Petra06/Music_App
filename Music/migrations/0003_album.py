# Generated by Django 3.1.2 on 2021-01-06 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=200)),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Music.year')),
            ],
        ),
    ]
