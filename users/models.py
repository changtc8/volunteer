from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    pmobile = models.CharField(max_length=12,null=True, blank=True)
    phome = models.CharField(max_length=12)
    pwork = models.CharField(max_length=12,null=True, blank=True)
    HOME = 'HM'
    WORK = 'WK'
    MOBILE = 'MO'
    PHONE_CHOICE = (
        (HOME, 'Home Phone'),
        (WORK, 'Work Phone'),
        (MOBILE, 'Mobile Phone'),
    )
    prefer_phone = models.CharField(max_length=2, choices=PHONE_CHOICE,
                                    default=MOBILE)
    def __unicode__(self):
        return self.email

class Ecalendar(models.Model):
    date = models.DateField('date published')
    time = models.TimeField() 
    def __unicode__(self):
        return self.date
  
class Event(models.Model):
    lead = models.ForeignKey(User)
    calendar = models.ForeignKey(Ecalendar)
    event_desc = models.CharField(max_length=40)
    addr = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    duration = models.IntegerField(default=1)
    def __unicode__(self):
        return self.event_desc

    


