from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ResourceCard(blocks.StructBlock):
	url = blocks.RichTextBlock(required=False)
	title = blocks.RichTextBlock(required=False)
	icon = ImageChooserBlock(required=False)

	class Meta:
		template = "streams/resource_card.html"
		icon = "edit"
		label = "Resource Card"

class ContentCard(blocks.StructBlock):
	title = blocks.RichTextBlock(required=False)
	descriptionOrContent = blocks.RichTextBlock(required=False)

	class Meta:
		template = "streams/content_card.html"
		icon = "icon"
		label = "Content Card"

