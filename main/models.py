from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from django.core.validators import EmailValidator


class RankModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Rank')
        verbose_name_plural = _('Ranks')


class TeamMember(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_("Full name"))
    image = models.ImageField(upload_to="images/", verbose_name=_("Image"))
    rank = models.ForeignKey(RankModel, on_delete=models.RESTRICT, verbose_name=_("Rank"))
    insta_url = models.URLField(verbose_name=_("Instagram URL"))
    facebook_url = models.URLField(verbose_name=_("Facebook URL"))
    twitter_url = models.URLField(verbose_name=_("Twitter URL"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')


class MessageModel(models.Model):
    user_name = models.CharField(max_length=100, verbose_name=_("Username"))
    email = models.EmailField(verbose_name=_("Email"), validators=[EmailValidator()])
    subject = models.CharField(max_length=255, verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ('-created_at',)