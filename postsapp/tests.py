from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    
    def test_view_url_exists_at_proper_location(self):
        respond = self.client.get('/')
        self.assertEqual(respond.status_code, 200)

    
    def test_view_by_usrl_name(self):
        respond = self.client.get(reverse('home'))
        self.assertEqual(respond.status_code, 200)

    
    def test_view_uses_correct_template(self):
        respond = self.client.get(reverse('home'))
        self.assertEqual(respond.status_code, 200)
        self.assertTemplateUsed(respond, 'home.html')