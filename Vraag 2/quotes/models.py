from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_bio = models.CharField(max_length=500)

    def __str__(self):
        return self.author_name


class Quote(models.Model):
    quote_text = models.CharField(max_length=300)
    quote_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text

    def search_quote(self, word):
        return word in self.quote_text


class Infraction(models.Model):
    id = 0
    year = models.CharField(max_length=300)
    month = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    street = models.CharField(max_length=300)
    driving_direction = models.CharField(max_length=300)
    speed_limit = models.CharField(max_length=300)
    passersby = models.CharField(max_length=300)
    infractions_speed = 0
    infractions_red_light = models.CharField(max_length=300)
