# Generated by Django 3.2.7 on 2022-08-14 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0082_blueflagsstep_monster1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueflagsstep',
            name='monster2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster2', to='front.monster'),
        ),
        migrations.AddField(
            model_name='blueflagsstep',
            name='monster3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster3', to='front.monster'),
        ),
        migrations.AddField(
            model_name='blueflagsstep',
            name='monster4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster4', to='front.monster'),
        ),
        migrations.AddField(
            model_name='blueflagsstep',
            name='monster5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster5', to='front.monster'),
        ),
        migrations.AlterField(
            model_name='blueflagsstep',
            name='monster1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster1', to='front.monster'),
        ),
    ]
