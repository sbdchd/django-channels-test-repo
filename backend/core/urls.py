from django.urls import path

import core.views

urlpatterns = [
    path(
        r"api/v1/calendar-presence/<team_pk>",
        core.views.presence,
        name="calendar-presence",
    )
]
