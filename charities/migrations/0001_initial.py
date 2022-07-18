# Generated by Django 4.0.6 on 2022-07-18 12:38

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
            name='Benefactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.SmallIntegerField(choices=[(0, 'beginner'), (1, 'intermediate'), (2, 'advance')], default=0)),
                ('free_time_per_week', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_limit_from', models.IntegerField(blank=True, null=True)),
                ('age_limit_to', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('gender_limit', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female')], max_length=1, null=True)),
                ('state', models.CharField(choices=[('P', 'Pending'), ('W', 'Waiting'), ('A', 'Assigned'), ('D', 'Done')], default='P', max_length=1)),
                ('title', models.CharField(max_length=60)),
                ('assigned_benefactor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='charities.benefactor')),
                ('charity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='charities.charity')),
            ],
        ),
    ]
