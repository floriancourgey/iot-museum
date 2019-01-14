import json
from django.test import TestCase, Client
from .models import Artwork

class AnimalTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        Artwork.objects.create(name='La Joconde', author='Leonard de Vinci')
        Artwork.objects.create(name='La nuit etoilee', author='Vincent Van Gogh')
        Artwork.objects.create(name='Londres, le Parlement', author='Claude Monet')

    def test_timesPlayed0(self):
        self.assertEqual(Artwork.objects.order_by('timesPlayed').first().timesPlayed, 0)
        self.assertEqual(Artwork.objects.order_by('timesPlayed').last().timesPlayed, 0)


    def test_next_timesPlayed(self):
        response = self.c.get('/next')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        response = self.c.get('/next')
        response = self.c.get('/next')
        self.assertEqual(Artwork.objects.order_by('timesPlayed').first().timesPlayed, 1)
        self.assertEqual(len(Artwork.objects.filter(timesPlayed=1)), 3)
