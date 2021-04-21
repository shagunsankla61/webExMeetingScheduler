from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from .forms import MeetingSchedulerForm
from .create_meeting_payload import payload, attendees, create_meeting


# Create your views here.

class LoginView(View):
    """."""

    template_name = 'webex_meeting_scheduler_app/login.html'

    def get(self, request, *args, **kwargs):
        """."""

        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form, 'link_name': 'Login', 'link_url': 'login.html'})

    def post(self, request, *args, **kwargs):
        """."""

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('create_meeting.html')
        else:
            messages.add_message(request, messages.INFO, 'Incorrect credentials')
            return redirect('login.html')


class LogoutView(View):
    """."""

    template_name = 'webex_meeting_scheduler_app/logout.html'

    def get(self, request, *args, **kwargs):
        """."""

        logout(request)
        return render(request, self.template_name, {'link_name': 'Login', 'link_url': 'login.html'})


class CreateMeeting(View):
    """."""
    template_name = 'webex_meeting_scheduler_app/create_meeting.html'

    @method_decorator(login_required(login_url='login.html'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """."""

        form = MeetingSchedulerForm()
        return render(request, self.template_name, {'form': form, 'link_name': 'Logout', 'link_url': 'logout.html'})

    def post(self, request, *args, **kwargs):
        """."""

        form = MeetingSchedulerForm(data=request.POST)
        if form.is_valid():
            attendees_xml = None
            attendee_emails = form.cleaned_data.get('attendee_email')
            attendee_names = form.cleaned_data.get('attendee_name')
            if attendee_emails and attendee_names:
                attendees_xml = ""
                attendee_emails = attendee_emails.split(',')
                attendee_names = attendee_names.split(',')
                if len(attendee_emails) > 1 and len(attendee_names) == len(attendee_emails):
                    for name, email in zip(attendee_names, attendee_emails):
                        attendees_xml += (
                                    attendees.format(attendee_name=name.strip(), attendee_email=email.strip()) + '\n')
                else:
                    attendees_xml = attendees.format(attendee_name=attendee_names[0].strip(),
                                                     attendee_email=attendee_emails[0].strip())

            _payload = payload.format(
                meeting_password=form.cleaned_data.get('password'),
                conf_name=form.cleaned_data.get('Title'),
                meeting_type=(1 if form.cleaned_data.get('meeting_type') else 0),
                agenda=form.cleaned_data.get('Agenda'),
                max_user=form.cleaned_data.get('max_user'),
                attendees=attendees_xml,
                chat=form.cleaned_data.get('chat'),
                auto_record=form.cleaned_data.get('enabledAutoRecordMeeting'),
                poll=form.cleaned_data.get('poll'),
                support=form.cleaned_data.get('support_encrypt'),
                auto_video=form.cleaned_data.get('auto_video'),
                start_date=form.cleaned_data.get('start_date'),
                open_time=form.cleaned_data.get('open_time'),
                join_teleconf=form.cleaned_data.get('join_teleconf'),
                duration=form.cleaned_data.get('duration'),
                time_zone_id=form.cleaned_data.get('time_zone_id'),
                phone_number=form.cleaned_data.get('phone_number')

            )
            print('########################################')
            print(_payload)
            print('########################################')

            response_status, response = create_meeting(_payload)
            print(response_status)
            print(response)

            form.save()
            messages.add_message(request, messages.INFO, 'Meeting Created Successfully')
            return redirect('create_meeting.html')
        else:
            messages.add_message(request, messages.INFO, 'Incorrect Data')
            return redirect('create_meeting.html')
