from django.test import SimpleTestCase # use simple testcase if u dont wanna interact with DB

from django.urls import reverse, resolve
from app.views import current_datetime,index

import app

class TestUrls(SimpleTestCase):
	def test_index_url_resolves(self):
		#assert 1 == 2
		url = reverse('index')
		self.assertEquals(resolve(url).func,index)


	def test_current_datetime_url_resolves(self):
		#assert 1 == 2
		url = reverse('current_datetime')
		self.assertEquals(resolve(url).func,current_datetime)
