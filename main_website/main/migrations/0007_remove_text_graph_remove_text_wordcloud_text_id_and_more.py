# Generated by Django 4.1.5 on 2023-04-30 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_text_id_text_graph_text_wordcloud_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='graph',
        ),
        migrations.RemoveField(
            model_name='text',
            name='wordcloud',
        ),
        migrations.AddField(
            model_name='text',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='text',
            name='text_title',
            field=models.CharField(max_length=20),
        ),
    ]
