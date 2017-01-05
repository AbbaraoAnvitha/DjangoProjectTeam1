from django.shortcuts import render
class BlogViewsTest(Testcase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

# Create your views here.
