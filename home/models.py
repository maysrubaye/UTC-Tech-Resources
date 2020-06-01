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
    desc = RichTextField(blank=True)
    service_card = StreamField([
    	("Service_Card", customBlocks.ServiceCard())], null=True, blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('heading'),
    	FieldPanel('desc'),
    	StreamFieldPanel('service_card')
    ]


class SingleServicePage(Page):
	backToMain = RichTextField(blank=True)
	heading = RichTextField(blank=True)
	steps = StreamField([
		("Step", customBlocks.StepCard())], null=True, blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('backToMain'),
		FieldPanel('heading'),
		StreamFieldPanel('steps')
	]

	search_fields = Page.search_fields + [ # Inherit search_fields from Page
        index.SearchField('heading', partial_match=True),
        index.SearchField('steps', partial_match=True),
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





