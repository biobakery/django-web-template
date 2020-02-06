import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from base import views

pytestmark = pytest.mark.django_db


class TestMyView:
    def test_anonymous(self):
        req = RequestFactory().get(reverse("base:home"))
        resp = views.MyView.as_view()(req)
        assert resp.status_code == 200