# Generated by Django 3.2.4 on 2021-06-29 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('date_established', models.DateField()),
            ],
            options={
                'verbose_name': 'College',
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('related_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='college.college')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('related_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='college.college')),
            ],
        ),
    ]
