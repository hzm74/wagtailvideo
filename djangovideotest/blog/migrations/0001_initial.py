# Generated by Django 5.1.4 on 2024-12-10 21:34

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        ('wagtaildocs', '0013_delete_uploadeddocument'),
        ('wagtailimages', '0026_delete_uploadedimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('wordcount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Word Count')),
                ('some_date', models.DateTimeField(blank=True, help_text='Some helpful text', null=True)),
                ('some_text', models.CharField(blank=True, default='some default value', max_length=255, null=True)),
                ('some_text_area', models.TextField(blank=True, null=True)),
                ('some_rich_text', wagtail.fields.RichTextField(blank=True, null=True)),
                ('some_slug', models.SlugField(blank=True, null=True)),
                ('some_choice_field', models.CharField(choices=[('a', 'Choice A'), ('b', 'Choice B'), ('c', 'Choice C')], default='a', max_length=255)),
                ('content', wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock())], blank=True, verbose_name='Page Content')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('some_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Some Document')),
                ('some_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Some Image')),
                ('some_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Some Page')),
            ],
            options={
                'verbose_name': 'Blog Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', wagtail.fields.RichTextField(blank=True, null=True)),
                ('some_date', models.DateTimeField(blank=True, help_text='Some helpful text', null=True)),
                ('some_text', models.CharField(default='some default value', max_length=255)),
                ('some_text_area', models.TextField(default='some default value')),
                ('some_choice_field', models.CharField(choices=[('a', 'Choice A'), ('b', 'Choice B'), ('c', 'Choice C')], default='a', max_length=255)),
                ('carousel_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carousel_image', to='wagtailimages.image', verbose_name='Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_images', to='blog.blogpage')),
            ],
            options={
                'verbose_name': 'Carousel Image',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
