from django.db import models

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.settings.models import BaseSiteSetting,register_setting



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
    ]

class Subscriber(models.Model):
    email = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    
    panels = [
        FieldPanel('email'),
        FieldPanel('full_name')
    ]

@register_setting
class SocialMediaSetting(BaseSiteSetting):
    facebook = models.URLField(blank=True, null= True, help_text='Facebook')
    youtube = models.URLField(blank=True, null=True, help_text='Youtube')

    panels = [
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('youtube')
        ], heading = "Social Media Setting")
    ]