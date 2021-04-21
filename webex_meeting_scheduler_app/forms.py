from django import forms
from .models import MeetingTable

from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget


class MeetingSchedulerForm(forms.ModelForm):
    """."""

    class Meta:
        """."""

        model = MeetingTable
        fields = ['Title', 'Agenda', 'password', 'meeting_type', 'max_user', 'attendee_name', 'attendee_email', 'chat',
                  'enabledAutoRecordMeeting', 'poll', 'support_encrypt', 'auto_video', 'start_date', 'open_time',
                  'join_teleconf', 'duration', 'time_zone_id', 'phone_number', 'User']

        widgets = {
            'Title': forms.Textarea(attrs={'rows': 3, 'cols': 100, 'length': 128, 'placeholder': 'Title for the Meeting'}),
            'Agenda': forms.Textarea(attrs={'rows': 3, 'cols': 130, 'length': 1300, 'placeholder': 'Agenda'}),
            'password': forms.PasswordInput(),
            'meeting_type': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'max_user': forms.NumberInput(attrs={'placeholder': 'Number Of User'}),
            'attendee_name': forms.TextInput(),
            'attendee_email': forms.TextInput({'placeholder': 'test@example.com'}),
            'chat': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'enabledAutoRecordMeeting': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'poll': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'support_encrypt': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'auto_video': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'start_date': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'length': 128, 'placeholder': 'e.g 4/21/2021 10:10:10'}),
            'open_time': forms.NumberInput(),
            'join_teleconf': DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
            'duration': forms.NumberInput(),
            'time_zone_id': forms.NumberInput(),
            'phone_number': forms.NumberInput(),
            'User': forms.HiddenInput()
        }
