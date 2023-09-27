import unittest
import requests
from unittest.mock import Mock, patch
from price_save import get_prices
from save_prices import get_prices_api


class TestGetPrices(unittest.TestCase):

    @patch('requests.get')
    def test_get_prices_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'data': ['price1', 'price2']}
        mock_get.return_value = mock_response

        result = get_prices()

        self.assertEqual(result, ['price1', 'price2'])

    @patch('requests.get')
    def test_get_prices_exception(self, mock_get):
        mock_get.side_effect = Exception("Something went wrong")

        result = get_prices()

        self.assertEqual(result, 'Something went wrong')


if __name__ == '__main__':
    unittest.main()
