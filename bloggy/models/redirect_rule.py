from django.db import models

from bloggy.models.mixin.updatable import Updatable


class RedirectRule(Updatable):
    from_url = models.CharField(max_length=300, help_text='Enter from url')
    to_url = models.CharField(max_length=300, help_text='Enter to url')
    status_code = models.IntegerField(
        default='standard', blank=True, null=True,
        choices=[
            (301, '301 Moved Permanently'),
            (307, '307 Temporary Redirect'),
        ],
        help_text="Redirect type",
        verbose_name="Redirect type")

    is_regx = models.BooleanField(
        default=False,
        null=True,
        help_text="Is this regx?"
    )

    note = models.CharField(
        max_length=500,
        help_text='Enter note',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.status_code}::{self.from_url}"


class Meta:
    verbose_name = "Redirect"
    verbose_name_plural = "Redirects"
