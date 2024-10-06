from django.test import TestCase
from .forms import CommentForm 

class TestCommentForm(TestCase):
    """
    Tests the CommentForm for validity.
    """

    def test_form_is_valid(self):
        """
        Test that a form with valid data is considered valid.
        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        """
        Test that a form without the 'body' field is invalid.
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid())
