"""Integration test for Github Wrapper."""
import pytest

from langchain.utilities.github import GitHubAPIWrapper
import logging
import logging

# Make sure you have set the following env variables:
# GITHUB_REPOSITORY_ENV
# GITHUB_BRANCH_ENV
# GITHUB_APP_ID
# GITHUB_PRIVATE_KEY


@pytest.fixture
def api_client(api_token: str = None, repository: str = 'owner/repo') -> GitHubAPIWrapper:
    return GitHubAPIWrapper()


def test_get_open_issues(api_client: GitHubAPIWrapper) -> None:
    """Test to fetch open issues when the repository does not exist"""
    issues = api_client.get_issues(filter='all', repository='nonexistent/repo')
    assert len(issues) == 0
    issues = api_client.get_issues(filter='all')
    assert len(issues) != 0
