from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ServiceCard(blocks.StructBlock):
	url = blocks.RichTextBlock(required=False)
	title = blocks.RichTextBlock(required=False)
	icon = ImageChooserBlock(required=False)

	class Meta:
		template = "streams/service_card.html"
		icon = "edit"
		label = "Resource Card"

class StepCard(blocks.StructBlock):
	title = blocks.RichTextBlock(required=False)
	descriptionOrContent = blocks.RichTextBlock(required=False)

	class Meta:
		template = "streams/step_card.html"
		icon = "icon"
		label = "Content Card"

