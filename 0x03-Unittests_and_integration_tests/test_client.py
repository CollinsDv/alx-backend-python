#!/usr/bin/env python3
"""
usage: client.GithubOrgClient class
"""
import unittest
import unittest.mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """testing GithubOrgClient class"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, get_json_mock):
        """tests org method
        """
        get_json_mock.return_value = {
            "payload": True
        }
        GithubOrgClient(org_name).org

        get_json_mock.assert_called_once()

    """
    memoize turns methods into properties(mock.PropertyMock).

    Implement the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url.

    Use patch as a context manager to patch GithubOrgClient.org and
        make it return a known payload.

    Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
    """
    def test_public_repos_url(self):
        """tests GithubOrgClient._public_repos_url"""
        with unittest.mock.patch("client.GithubOrgClient.org",
                                 new_callable=unittest.mock.PropertyMock
                                 ) as mock_org:
            mock_org.return_value = {"repos_url": True}

            assert GithubOrgClient('Google')._public_repos_url

    """
    Implement TestGithubOrgClient.test_public_repos to unit-test
        GithubOrgClient.public_repos.

    Use @patch as a decorator to mock get_json and make it return
        a payload of your choice.

    Use patch as a context manager to mock GithubOrgClient._public_repos_url
        and return a value of your choice.

    Test that the list of repos is what you expect from the chosen payload.

    Test that the mocked property and the mocked get_json was called once.
    """
    @unittest.mock.patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """testing public_repos method"""
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]
        with unittest.mock.patch("client.GithubOrgClient._public_repos_url",
                                 new_callable=unittest.mock.PropertyMock
                                 ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://example.com/repos"

            client = GithubOrgClient('google')
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])

            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
