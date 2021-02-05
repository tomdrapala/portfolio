from django.test import TestCase
from selenium import webdriver
from .models import Job

from django.core.files.uploadedfile import SimpleUploadedFile


# class FunctionalTestCase(TestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     def test_there_is_homepage(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         self.assertIn('Hi, my name is Tomasz.', self.browser.page_source)

#     def tearDown(self):
#         self.browser.quit()


class UnitTestCase(TestCase):
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'jobs/home.html')

    def saveJob(self):
        job = Job()
        job.title = 'test_job'
        job.summary = 'This is summary of test job'
        job.image = SimpleUploadedFile(name='test_image.jpg', content=open(r'.\images\fender.jpg', 'rb').read(), content_type='image/jpeg')
        job.save()
        return job

    def test_job_object(self):
        job = self.saveJob()
        pulled_job = Job.objects.get(title='test_job')
        self.assertEqual(job.title, pulled_job.title)
        self.assertEqual(job.summary, pulled_job.summary)
        self.assertEqual(job.image, pulled_job.image)
