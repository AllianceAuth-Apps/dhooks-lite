import json
from datetime import datetime
from unittest import TestCase

from dhooks_lite.embed import Author
from dhooks_lite.serializers import JsonDateTimeEncoder
from tests.utils import set_test_logger

MODULE_PATH = "dhooks_lite.serializers"
logger = set_test_logger(MODULE_PATH, __file__)


class TestJsonDateTimeEncoder(TestCase):
    def test_should_encode_datetime_without_error(self):
        # given
        my_date = datetime(2020, 8, 3, 16, 5, 0)
        my_dict = {"alpha": "dummy", "bravo": my_date}
        # when
        result = json.loads(json.dumps(my_dict, cls=JsonDateTimeEncoder))
        # then
        self.assertEqual(result, {"alpha": "dummy", "bravo": "2020-08-03T16:05:00"})

    def test_should_raise_error_for_unknown_type(self):
        # given
        my_dict = {"unknown": Author("dummy")}
        # when/then
        with self.assertRaises(TypeError):
            json.loads(json.dumps(my_dict, cls=JsonDateTimeEncoder))
