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

class staticQuiz(Page):
    pass





