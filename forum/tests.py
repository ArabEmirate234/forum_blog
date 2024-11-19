from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Thread, Post


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Test Category", description="A test category")
        self.thread = Thread.objects.create(
            title="Test Thread",
            content="This is a test thread",
            category=self.category,
            user=self.user
        )
        self.post = Post.objects.create(
            content="This is a test post",
            thread=self.thread,
            user=self.user
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "A test category")

    def test_thread_creation(self):
        self.assertEqual(self.thread.title, "Test Thread")
        self.assertEqual(self.thread.content, "This is a test thread")
        self.assertEqual(self.thread.category, self.category)

    def test_post_creation(self):
        self.assertEqual(self.post.content, "This is a test post")
        self.assertEqual(self.post.thread, self.thread)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Test Category", description="A test category")
        self.thread = Thread.objects.create(
            title="Test Thread",
            content="This is a test thread",
            category=self.category,
            user=self.user
        )
        self.post = Post.objects.create(
            content="This is a test post",
            thread=self.thread,
            user=self.user
        )

    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/homepage.html')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertTrue(response.url.endswith(reverse('homepage')))

    def test_like_post_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse('like_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)


class IntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Test Category", description="A test category")
        self.thread = Thread.objects.create(
            title="Test Thread",
            content="This is a test thread",
            category=self.category,
            user=self.user
        )

    def test_create_post_flow(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse('add_comment', args=[self.thread.id]), {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # Redirect after adding comment
        self.assertEqual(self.thread.posts.count(), 1)
        self.assertEqual(self.thread.posts.first().content, 'Test comment')
