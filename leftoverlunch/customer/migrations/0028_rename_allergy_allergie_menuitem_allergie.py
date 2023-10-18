# Generated by Django 4.2.5 on 2023-10-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0027_allergy_delete_allergies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Allergy',
            new_name='Allergie',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='allergie',
            field=models.ManyToManyField(related_name='items', to='customer.allergie'),
        ),
    ]
