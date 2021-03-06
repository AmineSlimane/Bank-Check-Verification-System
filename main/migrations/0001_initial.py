# Generated by Django 3.2.5 on 2022-05-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_original', models.ImageField(null=True, upload_to='original')),
                ('image_preprocessing', models.ImageField(null=True, upload_to='preprocessing')),
                ('image_with_bounding_boxes', models.ImageField(null=True, upload_to='bounding_boxes')),
                ('image_id', models.ImageField(null=True, upload_to='id')),
                ('image_nom', models.ImageField(null=True, upload_to='nom')),
                ('image_montant_chiffre', models.ImageField(null=True, upload_to='montant_chiffre')),
                ('image_montant_lettre', models.ImageField(null=True, upload_to='montant_lettre')),
                ('image_place', models.ImageField(null=True, upload_to='place')),
                ('image_date', models.ImageField(null=True, upload_to='date')),
                ('image_signature', models.ImageField(null=True, upload_to='signature')),
            ],
            options={
                'db_table': 'Cheque',
            },
        ),
    ]
