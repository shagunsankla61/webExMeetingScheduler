from django.urls import path
from .views import LoginView, LogoutView, CreateMeeting

app_name = 'webex_meeting_scheduler_app'

urlpatterns = [
    path('login.html', LoginView.as_view()),
    path('logout.html', LogoutView.as_view()),
    path('create_meeting.html', CreateMeeting.as_view())
]
