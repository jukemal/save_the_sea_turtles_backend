from django.db import models


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return 'District : ' + self.name


class SeaTurtleCount(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.ForeignKey(
        "app.District", on_delete=models.CASCADE)
    date = models.DateField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["district", "date"]
        unique_together = ['district', 'date']

    def __str__(self):
        return 'Sea Turtle Count : ' + self.district.name + ", " + str(self.date)
