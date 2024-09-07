#!/usr/bin/python3
"""
Script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys

def list_commits(repo_name, owner_name):
    # GitHub API URL for repository commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send GET request to the GitHub API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        commits = response.json()
        count = 0
        for commit in commits:
            if count >= 10:
                break
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
            count += 1
    else:
        print("Error fetching commits")

if __name__ == "__main__":
    # Get the repository name and owner name from command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo_name> <owner_name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        list_commits(repo_name, owner_name)
