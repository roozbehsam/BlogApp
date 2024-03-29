import pytest

from blog.fixtures.user import user
from blog.fixtures.post import post

from blog.comment.models import Comment


@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")
