from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class HoodTestClass(TestCase):
 
    def setUp(self):
        self.user = User.objects.create(id =1, username='mike')
        self.hood = Neighbourhood(name='kona mbaya', location='kasarani', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))

    
    def test_save_method(self):
        """
        Function to test that neighbourhood is being saved
        """
        self.hood.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.hood.save_hood()
        self.hood.delete_hood

    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.hood.save_hood()
        new_hood = Neighbourhood.objects.filter(name='mtaani').update(name='Bias')
        hoods = Neighbourhood.objects.get(name='Bias')
        self.assertTrue(hoods.name, 'Bias')

    
    def test_get_by_id(self):
        """
        Function to test if you can get a hood by its id
        """
        self.hood.save_hood()
        this_hood= self.hood.get_by_id(self.hood.id)
        hood = Neighbourhood.objects.get(id=self.hood.id)
        self.assertTrue(this_hood, hood)

    
class BusinessTestClass(TestCase):
    """
    Test business class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbourhood(name='mtaani', location='huko tu', user=self.user)
        self.hood.save_hood()
        self.biz = Business(name="bizna", email="evoh@gmail.com", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.biz, Business))

    
    def test_save_method(self):
        """
        Function to test that neighbourhood is being saved
        """
        self.biz.save_biz()
        bizes = Business.objects.all()
        self.assertTrue(len(bizes) > 0)


    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.biz.save_biz()
        new_biz = Business.objects.filter(name='bizna').update(name='biznas')
        bizes = Business.objects.get(name='biznas')
        self.assertTrue(bizes.name, 'biznas')


    def test_get_by_id(self):
        """
        Function to test if you can get a hood by its id
        """
        self.biz.save_biz()
        this_biz= self.biz.get_by_bizid(self.biz.id)
        biz = Business.objects.get(id=self.biz.id)
        self.assertTrue(this_biz, biz)



