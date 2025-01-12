# Generated by Django 3.2.23 on 2024-04-23 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_product_rating_and_feedback_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_table',
            old_name='product',
            new_name='PRODUCT',
        ),
        migrations.AddField(
            model_name='complaint_table',
            name='PRODUCT',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app2.product_table'),
            preserve_default=False,
        ),
    ]
