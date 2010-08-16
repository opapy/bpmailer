"""
Backend for test environment.
"""

from django.core import mail

from mailer.backends.base import BaseEmailBackend

class EmailBackend(BaseEmailBackend):
    """A email backend for use during test sessions.

    The test connection stores email messages in a dummy outbox,
    rather than sending them out on the wire.

    The dummy outbox is accessible through the outbox instance attribute.
    """
    def __init__(self, *args, **kwargs):
        super(EmailBackend, self).__init__(*args, **kwargs)
        if not hasattr(mail, 'outbox'):
            mail.outbox = []

    def _send_message(self, email_message):
        """Redirect messages to the dummy outbox"""
        mail.outbox.append(email_message)
