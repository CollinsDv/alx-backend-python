#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map

Test inputs:
    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """test class for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, _map, path, result):
        """takes parameterized args"""
        self.assertEqual(access_nested_map(_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, _map, path):
        """test exception raises"""
        with self.assertRaises(KeyError):
            access_nested_map(_map, path)


class TestGetJson(unittest.TestCase):
    """tests utils.get_json"""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('utils.requests.get')
    def test_get_json(self, link, payload, mock_get):
        """mocks HTTP requests
        """
        response_mock = unittest.mock.Mock()
        response_mock.json.return_value = payload
        mock_get.return_value = response_mock

        assert get_json(link) == payload
        mock_get.assert_called_once()
        mock_get.assert_called_with(link)
