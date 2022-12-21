from django.test import TestCase

from django.contrib.auth.models import User
from maps.models import Campaign

# Create your tests here.

class TestCampaign(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        bob = User.objects.create(username='bob', password='password12')
        Campaign.objects.create(
            user=bob,
            title='Curse of Bob',
            description='A story of love and betrayal, with magic and dragons too!')
        pass

    # Data/Field Tests for Campaign
    def test_title_data(self):
        campaign = Campaign.objects.get(id=1)
        title_label = campaign._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')
        self.assertEqual(campaign.title, 'Curse of Bob')

    def test_user_assignment(self):
        campaign = Campaign.objects.get(id=1)
        user = campaign.user
        bob = User.objects.get(id=1)
        self.assertEqual(user, bob)
        self.assertEqual(user.username, 'bob')
        self.assertEqual(user.password, 'password12')

    def test_description_data(self):
        campaign = Campaign.objects.get(id=1)
        desc_label = campaign._meta.get_field('description').verbose_name
        self.assertEqual(desc_label, 'description')
        self.assertEqual(campaign.description, 'A story of love and betrayal, with magic and dragons too!')

    # Edge Case Tests for Campaign
    """
    def test_title_maximum(self):
        title_too_long = Campaign.objects.create(
            user=User.objects.get(id=1),
            title="This title is far too long, even though we specified a maximum of 100 chars, which no one should need",
            description="It really shouldn't matter at this point"
        )
        title_too_long.save()
        """
