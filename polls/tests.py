from django.test import TestCase

from polls.models import Choice
from polls.models import Question


class PollsTest(TestCase):
    """Test cases for Questions and Choices."""

    def test_question(self):
        """Tests questions and choices can be created and endure."""
        self.q1 = Question.objects.create(
            question_text="What's up?",
            pub_date="2000-01-01",
        )
        self.c1 = Choice.objects.create(
            question=self.q1,
            choice_text="The sky",
        )

        self.assertEqual(self.q1.question_text, "What's up?")
        self.assertEqual(self.c1.choice_text, "The sky")
        self.assertEqual(self.c1.question, self.q1)
