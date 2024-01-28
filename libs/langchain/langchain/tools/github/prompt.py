# flake8: noqa
GET_ISSUES_PROMPT = """
This tool will fetch a list of the repository's issues. It will return the title, issue number, and body of 5 issues. It takes no input.

Example: No input required."""

GET_ISSUE_PROMPT = """
This tool will fetch the title, body, and comment thread of a specific issue. **VERY IMPORTANT**: You must specify the issue number as an integer.
"""

COMMENT_ON_ISSUE_PROMPT = """
This tool is useful when you need to comment on a GitHub issue. Simply pass in the issue number and the comment you would like to make. 

**Input requirements:**
- Specify the issue number as an integer
- Place two newlines
- Specify your comment

Example:
1

This is a comment."""
CREATE_PULL_REQUEST_PROMPT = """
This tool is useful when you need to create a new pull request in a GitHub repository.

**Input requirements:**
- Specify the title of the pull request
- Place two newlines
- Write the body or description of the pull request

To reference an issue in the body, put its issue number directly after a #.

Example:
README updates

Added contributors' names, closes issue #3"""
CREATE_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to create a file in a GitHub repository.

**Input requirements:**
- Specify the file to create by passing a full file path (**IMPORTANT**: the path must not start with a slash)
- Specify the contents of the file

Example:
test/test.txt

test contents"""

READ_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to read the contents of a file in a GitHub repository.

**Input requirements:**
- Specify the full file path of the file you would like to read. (**IMPORTANT**: the path must not start with a slash)

Example:
test/test.txt"""

UPDATE_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to update the contents of a file in a GitHub repository.

**Input requirements:**
- Specify which file to modify by passing a full file path (**IMPORTANT**: the path must not start with a slash)
- Specify the old contents to replace wrapped in OLD <<<< and >>>> OLD
- Specify the new contents to replace wrapped in NEW <<<< and >>>> NEW

For example, if you would like to replace the contents of the file test/test.txt from "old contents" to "new contents", you would pass in the following string:

test/test.txt

This is text that will not be changed
OLD <<<<
old contents
>>>> OLD
NEW <<<<
new contents
>>>> NEW"""

DELETE_FILE_PROMPT = """
This tool is a wrapper for the GitHub API, useful when you need to delete a file in a GitHub repository. 

**Input requirements:**
- Specify the full file path of the file you would like to delete. (**IMPORTANT**: the path must not start with a slash)

Example:
test/test.txt"""
