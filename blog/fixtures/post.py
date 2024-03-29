import pytest

from blog.fixtures.user import user
from blog.post.models import Post


@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body="Test Post Body")