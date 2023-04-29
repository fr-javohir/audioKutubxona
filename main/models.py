from django.db import models
class Topic(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Audio(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    duration = models.CharField(max_length=25,blank=True, null=True)
    size = models.CharField(max_length=20,blank=True,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    def __str__(self):
        return self.title