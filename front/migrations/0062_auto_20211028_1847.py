# Generated by Django 3.2.7 on 2021-10-28 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0061_auto_20211026_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guide',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='companion',
            name='armor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companion',
            name='convenience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companion',
            name='life',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companion',
            name='lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companion',
            name='stamina',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companion',
            name='weapon_lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CompanionSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus', models.IntegerField()),
                ('adventure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.adventure')),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.companion')),
                ('crafting', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.crafting')),
                ('gathering', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.gathering')),
                ('land', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.land')),
            ],
        ),
    ]
