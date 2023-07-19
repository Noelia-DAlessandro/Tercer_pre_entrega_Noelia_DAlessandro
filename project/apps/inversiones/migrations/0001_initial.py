# Generated by Django 4.2.3 on 2023-07-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentoFinanciero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('plazo_fijo', 'Plazo fijo'), ('bonos', 'Bonos'), ('acciones', 'Acciones')], max_length=20)),
                ('tipo_cambio', models.CharField(choices=[('pesos', 'Pesos'), ('dolares', 'Dólares')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInversor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('conservador', 'Conservador'), ('agresivo', 'Agresivo')], max_length=20)),
            ],
        ),
    ]
