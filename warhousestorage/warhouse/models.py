from django.db import models

class Rodzajdokumentu(models.Model):
				nazwa = models.CharField(max_length=255)
				
				class Meta:
						verbose_name_plural = "Rodzaje dokumentow"
				