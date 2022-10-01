from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoices(TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    BLOCKED = 'BLOCKED', 'Blocked'


class Book(models.Model):
    status = models.CharField(verbose_name='Status', choices=StatusChoices.choices, max_length=200,
                              default=StatusChoices.ACTIVE)
    name = models.CharField(verbose_name='Name', max_length=200, null=False, blank=False)
    email = models.EmailField(verbose_name='Email', max_length=260, null=False, blank=False)
    text = models.TextField(verbose_name='Text', max_length=3000, null=False, blank=False)
    author = models.CharField(verbose_name='Author', max_length=200, null=False, blank=False, default='No name')
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)

    def __str__(self):
        return f'{self.name} - {self.email}- {self.author}'


    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

