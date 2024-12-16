import unittest
from unittest.mock import patch, create_autospec, Mock

from requests.exceptions import Timeout

from ex1 import get_time, requests, A

class MockExamples(unittest.TestCase):
    @patch("ex1.requests")
    def test_get_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_time()
                mock_requests.get.assert_called_once()

    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_time()

    def test_spec(self):
        #mock = Mock()
        mock = create_autospec(A)
        mock.f1(1, 2, 3)
        mock.f1.assert_called_once()
        #mock.f1.assert_called_with(a=1, b=2, c=3)


if __name__ == "__main__":
    unittest.main()