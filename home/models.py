from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks, hooks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from utcTechSources import customBlocks
from wagtail.search import index


class HomePage(Page):
    heading = RichTextField(blank=True)
    description = RichTextField(blank=True)
    resource_card = StreamField([
    	("Resource_Card", customBlocks.ResourceCard())], null=True, blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('heading'),
    	FieldPanel('description'),
    	StreamFieldPanel('resource_card')
    ]


class SingleResourcePage(Page):
	heading = RichTextField(blank=True)
	content = StreamField([
		("Content_Card", customBlocks.ContentCard())], null=True, blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('heading'),
		StreamFieldPanel('content')
	]

	search_fields = Page.search_fields + [ # Inherit search_fields from Page
        index.SearchField('heading', partial_match=True),
        index.SearchField('content', partial_match=True),
    ]

class Quiz(Page):
    top_descriptions = RichTextField(blank=True)
    first_q = RichTextField(blank=True)
    ten_year_q = RichTextField(blank=True)
    gpa_q = RichTextField(blank=True)
    country_q = RichTextField(blank=True)
    no_test_result = RichTextField(blank=True)
    esl_result = RichTextField(blank=True)
    math_egl_result = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('top_descriptions'),
        FieldPanel('first_q'),
        FieldPanel('ten_year_q'),
        FieldPanel('gpa_q'),
        FieldPanel('country_q'),
        FieldPanel('no_test_result'),
        FieldPanel('math_egl_result'),
        FieldPanel('esl_result'),
    ]





