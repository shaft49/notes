## GITHUB CLI
Go to this [link](https://cli.github.com/manual/) for detailed documentation.

# Installation
Go to this [link](https://github.com/cli/cli#installation) to find out os specific installation

# Authentication, either by auth token or by browser

    gh auth login

# Set Editor
    gh config set editor code # if you wanna use the visual studio code

# Create Issues

     gh issue create --title "I found a bug" --body "Nothing works" --label bug

     or

     gh issue create --web # it will open the issue page in the browser
# Close Issue
    gh issue close {issue_url}

# Pull Request

    gh pr create # Interactive Pull Request
    
# Merge Request

    gh pr merge # Interactive merging
