# Generated by Django 2.1.4 on 2019-07-12 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songid', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'song',
            },
        ),
        migrations.CreateModel(
            name='Songlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listname', models.CharField(max_length=200)),
                ('isdelete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'songlist',
            },
        ),
        migrations.AddField(
            model_name='song',
            name='songlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Songlist'),
        ),
    ]
