# Generated by Django 3.2.5 on 2021-09-11 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Carrito', '0008_auto_20210821_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]