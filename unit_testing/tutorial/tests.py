import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
      # 関数内でimportすることで、テストを分離することができる (import は他のテストの破壊をしかねない)　
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
