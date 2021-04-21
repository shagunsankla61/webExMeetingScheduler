from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MeetingTable(models.Model):
    """."""

    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.TextField()
    meeting_type = models.BooleanField()
    max_user = models.IntegerField()
    attendee_name = models.TextField()
    attendee_email = models.TextField()
    chat = models.BooleanField()
    poll = models.BooleanField()
    support_encrypt = models.BooleanField()
    auto_video = models.BooleanField()
    Agenda = models.TextField()
    password = models.CharField(max_length=50)
    start_date = models.TextField()
    open_time = models.IntegerField()
    join_teleconf = models.BooleanField()
    enabledAutoRecordMeeting = models.BooleanField()
    duration = models.IntegerField()
    time_zone_id = models.IntegerField()
    phone_number = models.IntegerField()


class Meta:
    """."""
    db_table = 'MeetingTable'
