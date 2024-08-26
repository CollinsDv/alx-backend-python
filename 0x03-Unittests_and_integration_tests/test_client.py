#!/usr/bin/env python3
"""
usage: client.GithubOrgClient class
"""
import unittest
import unittest.mock
from client import GithubOrgClient
from parameterized import parameterized
from requests import HTTPError


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

    """
    Implement TestGithubOrgClient.test_has_license to unit-test
        GithubOrgClient.has_license.

    Parametrize the test with the following inputs

    repo={"license": {"key": "my_license"}}, license_key="my_license"
    repo={"license": {"key": "other_license"}}, license_key="my_license"
    You should also parameterize the expected returned value.
    """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repos, license, expected):
        """tests GithubOrgClient.has_license"""
        assert GithubOrgClient('any').has_license(
            repos, license) == expected


"""
We want to test the GithubOrgClient.public_repos method in an
    integration test. That means that we will only mock code that
    sends external requests.

Create the TestIntegrationGithubOrgClient(unittest.TestCase)
    class and implement the setUpClass and tearDownClass which
    are part of the unittest.TestCase API.

Use @parameterized_class to decorate the class and parameterize
    it with fixtures found in fixtures.py. The file contains the
    following fixtures:
    org_payload, repos_payload, expected_repos, apache2_repos

The setupClass should mock requests.get to return example payloads
    found in the fixtures.

Use patch to start a patcher named get_patcher, and use side_effect
    to make sure the mock of requests.get(url).json() returns the
    correct fixtures for the various values of url that you anticipate
    to receive.

Implement the tearDownClass class method to stop the patcher.
"""
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return unittest.mock.Mock(
                    **{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = unittest.mock.patch(
            "requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
