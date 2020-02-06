import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestMyModel:
    def test_mymodel(self):
        assert 1 == 1, "Should create a MyModel instance"