# Generated by Django 4.2.5 on 2023-09-07 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('EmpCode', models.CharField(max_length=50)),
                ('Mobiel_No', models.CharField(max_length=50)),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataRegister.position')),
            ],
        ),
    ]
