import unittest
from unittest.mock import patch
from app import app, Batch


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.connection.execute')
    def test_no_params_selected(self, mock_execute):
        mock_execute.return_value.fetchall.return_value = []
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "No params were selected")

    @patch('app.connection.execute')
    def test_filter_with_params(self, mock_execute):
        mock_batch1 = Batch(batch_number=1, submitted_at="2018-01-01T00:00:00", nodes_used=5)
        mock_batch2 = Batch(batch_number=2, submitted_at="2018-02-01T00:00:00", nodes_used=8)
        mock_execute.return_value.fetchall.return_value = [mock_batch1, mock_batch2]

        response = self.app.get('/?min_nodes=2&max_nodes=10&submitted_after=2018-01-01T00:00:00&submitted_before=2019-01-01T00:00:00')
        self.assertEqual(response.status_code, 200)

    @patch('app.connection.execute')
    def test_filter_with_min_nodes_param(self, mock_execute):
        mock_batch1 = Batch(batch_number=1, submitted_at="2018-01-01T00:00:00", nodes_used=5)
        mock_batch2 = Batch(batch_number=2, submitted_at="2018-02-01T00:00:00", nodes_used=8)
        mock_execute.return_value.fetchall.return_value = [mock_batch1, mock_batch2]

        response = self.app.get('/?min_nodes=5')
        self.assertEqual(response.status_code, 200)

    @patch('app.connection.execute')
    def test_filter_with_max_nodes_param(self, mock_execute):
        mock_batch1 = Batch(batch_number=1, submitted_at="2018-01-01T00:00:00", nodes_used=5)
        mock_batch2 = Batch(batch_number=2, submitted_at="2018-02-01T00:00:00", nodes_used=8)
        mock_execute.return_value.fetchall.return_value = [mock_batch1, mock_batch2]

        response = self.app.get('/?max_nodes=10')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
