# Generated by Django 4.0.4 on 2022-04-24 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Population', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataType', models.CharField(max_length=30)),
                ('MainLocation', models.CharField(max_length=30)),
                ('Capital', models.CharField(max_length=30)),
                ('Population', models.FloatField(default=0)),
                ('Language', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Table6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=30)),
                ('Capital', models.CharField(max_length=30)),
                ('foreign_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CountryApp.population')),
                ('foreign_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CountryApp.language')),
            ],
        ),
        migrations.CreateModel(
            name='Table5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=30)),
                ('Capital', models.CharField(max_length=30)),
                ('foreign_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CountryApp.population')),
                ('foreign_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CountryApp.language')),
            ],
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=30)),
                ('Capital', models.CharField(max_length=30)),
                ('foreign_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CountryApp.population')),
                ('foreign_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CountryApp.language')),
            ],
        ),
    ]
