# Generated by Django 2.2.5 on 2019-09-11 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rateme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rateme.RatingCard')),
            ],
        ),
    ]
