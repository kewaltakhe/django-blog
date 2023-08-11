from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse
# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.test_post = Post.objects.create(
            title = 'a nice title',
            author = self.user,
            body = 'a nice body'
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.test_post.get_absolute_url(),'/post/1/')

    def test_string_representation(self):
        post = Post(title='a sample title')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.test_post.title}','a nice title')
        self.assertEqual(f'{self.test_post.body}','a nice body')
        self.assertEqual(f'{self.test_post.author}','testuser')

    def test_home_view_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'a nice body')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view_page(self):
        response = self.client.get('/post/1/')
        invalid_response = self.client.get('/post/100000',follow=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(invalid_response.status_code,404)
        self.assertTemplateUsed(response,'post_detail.html')
        self.assertContains(response,'a nice title')

    def test_post_create_view_page(self):
        response = self.client.post(reverse('new_post'),
                                    {
                                        'title':'new title',
                                        'body':'new body',
                                        'author':self.user.id
                                    })
        self.assertEqual(response.status_code,302)
        #self.assertTemplateUsed(response,'new_post.html') # Does not work AssertionError: No templates used to render the response
        Post.objects.last().title = 'new title'
        Post.objects.last().body = 'new body'

    def test_post_edit_view_page(self):
        response = self.client.post(reverse('post_edit',args='1'),
                                    {
                                        'title':'updated_title',
                                        'body':'updated_body'
                                    })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title,'updated_title')
        self.assertEqual(Post.objects.last().body, 'updated_body')

    def test_post_delete_view_page(self):
        response = self.client.post(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code,302)
