"""Integration test for Github Wrapper."""
import pytest

from langchain.utilities.github import GitHubAPIWrapper

# Make sure you have set the following env variables:
# GITHUB_REPOSITORY
# GITHUB_BRANCH
# GITHUB_APP_ID
# GITHUB_PRIVATE_KEY


@pytest.fixture
def api_client() -> GitHubAPIWrapper:
    return GitHubAPIWrapper()


def test_get_open_issues(api_client: GitHubAPIWrapper) -> None:
    """Test fetching open issues"""
    # Test case: no open issues
    issues = api_client.get_issues()
    assert len(issues) == 0

    # Test case: 1 open issue
    # Simulate fetching one open issue and check the result
    issue_1 = {'title': 'Test issue 1', 'body': 'This is a test issue', 'number': 1}
    api_client.get_issues = lambda: [issue_1]
    issues = api_client.get_issues()
    assert len(issues) == 1
    assert issues[0] == issue_1

    # Test case: error during issue fetching
    # Simulate an error during issue fetching and check if an exception is raised
    api_client.get_issues = lambda: Exception('Error fetching issues')
    with pytest.raises(Exception):
        api_client.get_issues()

    # Test case: 1 open issue
    # Simulate fetching one open issue and check the result
    issue_1 = {'title': 'Test issue 1', 'body': 'This is a test issue', 'number': 1}
    api_client.get_issues = lambda: [issue_1]
    issues = api_client.get_issues()
    assert len(issues) == 1
    assert issues[0] == issue_1

    # Test case: error during issue fetching
    # Simulate an error during issue fetching and check if an exception is raised
    api_client.get_issues = lambda: Exception('Error fetching issues')
    with pytest.raises(Exception):
        api_client.get_issues()
    assert len(issues) != 0
