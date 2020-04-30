from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

def foto_path(instance, filename):
    return "sk/" + str(instance.id) + "/foto" + filename

class Druzstva(models.Model):
    oznaceni = models.CharField(max_length=10,
                                choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")])

    class Meta:
        ordering = ["oznaceni"]
        verbose_name_plural = "Družstva"

class Status(models.Model):
    nazev = models.CharField(max_length=30, blank=True, verbose_name="Název")

    class Meta:
        ordering = ["nazev"]
        verbose_name_plural = "Status"

class Prispevky(models.Model):
    castka = models.DecimalField(max_digits=7,decimal_places=2, verbose_name="Částka")
    datum_platby = models.DateField(help_text="Formát: RRRR-MM-DD", verbose_name="Datum platby")

    class Meta:
        ordering = ["castka", "datum_platby"]
        verbose_name_plural = "Příspěvky"

class Clen(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=50, verbose_name="Příjmení")
    vek = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(100)], verbose_name="Věk")
    datum_vstupu = models.DateField(null=True, help_text="Formát: RRRR-MM-DD", verbose_name="Datum vstupu")
    foto = models.ImageField(upload_to=foto_path, null=True, blank=True ,verbose_name="Fotka")
    druzstvo = models.ManyToManyField(Druzstva)
    status = models.ManyToManyField(Status)
    platba = models.ManyToManyField(Prispevky)

    class Meta:
        ordering = ["prijmeni"]
        verbose_name_plural = "Člen"