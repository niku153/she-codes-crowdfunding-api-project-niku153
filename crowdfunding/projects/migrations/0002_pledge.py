# Generated by Django 4.1.5 on 2023-01-14 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('anonymous', models.BooleanField()),
                ('supporter', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.project')),
            ],
        ),
    ]
