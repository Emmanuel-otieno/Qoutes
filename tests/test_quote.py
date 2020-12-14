from app.models import Comment,User,Quote
from app import db
import unittest

class QuoteModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Emmanuel = User(username = 'Emmanuel',password = '0725939687', email = 'sakoemmanuel4@gmail.com')
        self.new_quote = Quote(id=1,quote_title='Test',quote_content='This is a test pitch',category="interview",user = self.user_Emmanuel,likes=0,dislikes=0)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_quote.quote_title,'Test')
        self.assertEquals(self.new_quote.quote_content,'This is a test pitch')
        self.assertEquals(self.new_quote.category,"interview")
        self.assertEquals(self.new_quote.user,self.user_Emmanuel)

    def test_save_quote(self):
        self.new_quote.save_qoute()
        self.assertTrue(len(Quote.query.all())>0)

    def test_get_quote_by_id(self):
        self.new_quote.save_qoute()
        get_quote = Quote.get_quote(1)
        self.assertTrue(got_qoutr is not None)