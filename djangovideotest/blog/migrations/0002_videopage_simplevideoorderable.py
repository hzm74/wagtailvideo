# Generated by Django 5.1.4 on 2024-12-16 21:19

import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.routable_page.models
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(verbose_name='Introduction')),
            ],
            options={
                'verbose_name': 'Video Page',
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='SimpleVideoOrderable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('url', models.URLField()),
                ('description', wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='blog.videopage')),
            ],
            options={
                'verbose_name': 'Video',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
