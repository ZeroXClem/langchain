"""
This tool allows agents to interact with the pygithub library
and operate on a GitHub repository.

To use this tool, you must first set as environment variables:
    GITHUB_API_TOKEN
    GITHUB_REPOSITORY -> format: {owner}/{repo}

"""
from typing import Optional

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.pydantic_v1 import Field
from langchain.tools.base import BaseTool
from langchain.utilities.github import GitHubAPIWrapper


class GitHubAction(BaseTool):
    """Tool for interacting with the GitHub API."""

    api_wrapper: GitHubAPIWrapper = Field(default_factory=GitHubAPIWrapper)
    mode: str
    name: str = ""
    description: str = ""

    def _run(
        self,
        instructions: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the GitHub API to run an operation."""
        if 'workload_identity_provider' not in instructions and 'credentials_json' not in instructions:
            raise ValueError('One of workload_identity_provider or credentials_json must be provided.')

        if 'workload_identity_provider' in instructions and 'credentials_json' in instructions:
            raise ValueError('Only one of workload_identity_provider or credentials_json should be provided.')

        # Ensure that necessary input values are injected into the environment when using GitHub secrets
        # Update the error message to provide clear instructions on how to resolve the issue
