# Generated by Django 2.2.9 on 2020-06-01 00:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200531_0456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='countryQ',
            new_name='country_q',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='firstQ',
            new_name='first_q',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='gpaQ',
            new_name='gpa_q',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='tenYearQ',
            new_name='ten_year_q',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='topDescriptions',
            new_name='top_descriptions',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='options',
        ),
        migrations.AddField(
            model_name='quiz',
            name='country_q_options',
            field=wagtail.core.fields.StreamField([('options', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='first_q_options',
            field=wagtail.core.fields.StreamField([('options', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='gpa_q_options',
            field=wagtail.core.fields.StreamField([('options', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='ten_year_q_options',
            field=wagtail.core.fields.StreamField([('options', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='result',
            field=wagtail.core.fields.StreamField([('result', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
