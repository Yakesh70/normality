from django.test import TestCase, Client
from django.urls import reverse
import numpy as np

class NormalityTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_analyze_view_get(self):
        """Test that the form loads correctly"""
        response = self.client.get(reverse('analyze'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Normality Testing Tool')
        
    def test_analyze_view_post_valid(self):
        """Test analysis with valid data"""
        # Normal-ish data
        data = {
            'numbers': '1.2, 2.1, 1.8, 2.3, 1.9, 2.0, 1.7, 2.2, 1.6, 2.4, 1.5'
        }
        response = self.client.post(reverse('analyze'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Summary Statistics')
        self.assertContains(response, 'Shapiro')
        
    def test_analyze_view_post_invalid(self):
        """Test analysis with invalid data"""
        data = {
            'numbers': '1, 2, 3'  # Too few numbers
        }
        response = self.client.post(reverse('analyze'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter between 10 and 15 numbers')
        
    def test_form_validation(self):
        """Test form validation with various inputs"""
        from .forms import NumbersForm
        
        # Valid input
        form = NumbersForm({'numbers': '1,2,3,4,5,6,7,8,9,10,11'})
        self.assertTrue(form.is_valid())
        
        # Invalid input - too few numbers
        form = NumbersForm({'numbers': '1,2,3'})
        self.assertFalse(form.is_valid())
        
        # Invalid input - non-numeric
        form = NumbersForm({'numbers': '1,2,3,abc,5,6,7,8,9,10,11'})
        self.assertFalse(form.is_valid())