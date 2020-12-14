from app.models import Comment,User,Quote
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Emmanuel = User(username = 'Emmanuel',password = '0725939687', email = 'sakoemmanuel4@gmail.com')
        self.new_quote = Quote(id=1,quote_title='Test',quote_content='This is a test quote',category="interview",user = self.user_Emmanuel,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_Emmanuel,quote=self.new_quote)

    def tearDown(self):
        Quote.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Emmanuel)
        self.assertEquals(self.new_comment.quote,self.new_qoute)