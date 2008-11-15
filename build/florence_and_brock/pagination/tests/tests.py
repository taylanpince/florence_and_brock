from django.test import TestCase, Client
from django.conf import settings
from django.core.urlresolvers import reverse

from pagination.settings import PAGINATION_MAX_PAGES
from pagination.tests.models import TestModel


class TestComment(TestCase):

    def setUp(self):
        pass

    def testPageControlDisplay(self):
        # Page controls should only be displayed if there is more
        # than one page
        for i in range(settings.PAGINATE_BY):
            TestModel.objects.create()
        response = self.client.get('/list/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertNotContains(response, 'first')
        TestModel.objects.create()
        response = self.client.get('/list/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'first')
        self.assertContains(response, '1')
        self.assertContains(response, 'last')


    def testMaxPages(self):
        for i in range(PAGINATION_MAX_PAGES * settings.PAGINATE_BY):
            TestModel.objects.create()
        response = self.client.get('/list/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'first')
        self.assertContains(response, '1')
        self.assertContains(response, 'last')
        self.assertNotContains(response, '&#0133;')
        TestModel.objects.create()
        response = self.client.get('/list/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, '&#0133;')

    def testEmptyBaseUrl(self):
        for i in range(settings.PAGINATE_BY + 1):
            TestModel.objects.create()
        response = self.client.get('/list/')
        self.assertContains(response, 'href="/list/?page=2"')
        response = self.client.get('/list/', {'q' : 'test'})
        self.assertContains(response, 'href="/list/?q=test&amp;page=2"')


