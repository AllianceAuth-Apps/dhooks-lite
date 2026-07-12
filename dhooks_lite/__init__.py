"""A wrapper for sending messages to Discord webhooks."""

from .client import UserAgent, Webhook, WebhookResponse
from .embed import Author, Embed, Field, Footer, Image, Thumbnail

__version__ = "1.1.0"
__title__ = "dhooks_lite"
__url__ = "https://github.com/AllianceAuth-Apps/dhooks-lite"

__all__ = [
    "UserAgent",
    "Webhook",
    "WebhookResponse",
    "Author",
    "Embed",
    "Field",
    "Footer",
    "Image",
    "Thumbnail",
]
