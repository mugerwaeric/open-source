# Generated by Django 2.2.2 on 2019-06-27 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190628_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knockout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='away_matches', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='app.Group'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_matches', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='app.Group'),
        ),
        migrations.AddField(
            model_name='match',
            name='knockout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='app.Knockout'),
        ),
    ]
