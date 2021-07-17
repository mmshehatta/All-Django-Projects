from django.test import TestCase
from .models import Post
from django.urls import reverse #new
# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text1='just a test')

    def test_text1_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text1}'
        self.assertEqual(expected_object_name , 'just a test')


class HomePageViewTest(TestCase):

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code , 200)
        self.assertTemplateUsed(resp , 'home.html')


