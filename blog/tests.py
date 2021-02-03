from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'password'
        )
        self.post = Post.objects.create(
            title  = 'Title',
            body  = 'Body',
            author = self.user
        )

    
    def test_string_representation(self):
        post = Post(title = "simple title")
        self.assertEqual(str(post),post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_model_content(self):
        self.assertEqual(f'{self.post.title}', 'Title')
        self.assertEqual(f'{self.post.body}', 'Body')
        self.assertEqual(f'{self.post.author}', 'testuser')


class IndexViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser', 
            email = 'test@email.com',
            password = 'password')
        self.post = Post.objects.create(
            title  = 'Title',
            body  = 'Body',
            author = self.user
        )    

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Body')
        self.assertTemplateUsed(response, 'blog/index.html')


class DetailViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser', 
            email = 'test@email.com',
            password = 'password')
        self.post = Post.objects.create(
            title  = 'Title',
            body  = 'Body',
            author = self.user
        )

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response , 'Title')
        self.assertTemplateUsed(response , 'blog/pos_detail.html')


class CreateViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'password'
        )

    def test_post_creation(self):
        response = self.client.post(reverse('blog:new'), {
            'title':'New title',
            'body': 'New body',
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New body')


class UpdateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'test@email.com',
            password = 'password'
        )
        self.post = Post.objects.create(
            title = 'Title',
            body = 'Body',
            author = self.user
        )

    def test_post_update_view(self):
        response = self.client.post(reverse('blog:post_edit', args = '1'),{
            'title':'Updated title',
            'body': 'Updated body'})
        self.assertEqual(response.status_code, 302)

    def  test_post_updated_content(self):
        response = self.client.get('/post/1/')
        self.assertContains(response , 'Title')
        self.assertContains(response , 'Body')


class DeleteViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'test@email.com',
            password = 'password'
        )
        self.post = Post.objects.create(
            title = 'title',
            body= 'body',
            author = self.user
        )
    def test_post_delete_view(self): 
        response = self.client.post(reverse('blog:post_delete', args = '1'))
        self.assertEqual(response.status_code, 302)
    






