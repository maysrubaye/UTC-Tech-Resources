from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ServiceCard(blocks.StructBlock):
	url = blocks.RichTextBlock(required=False)
	name = blocks.RichTextBlock(required=False)
	icon = ImageChooserBlock(required=False)

	class Meta:
		template = "streams/service_card.html"
		icon = "edit"
		label = "Service Card"

class StepCard(blocks.StructBlock):
	step_num = blocks.RichTextBlock(required=False)
	desc = blocks.RichTextBlock(required=False)

	class Meta:
		template = "streams/step_card.html"
		icon = "icon"
		label = "Step Card"

