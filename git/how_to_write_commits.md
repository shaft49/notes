# How to Write Git Commits
- [x] [The seven rules of a great Git commit message](https://chris.beams.io/posts/git-commit/)

1. Separate subject from body with a blank line
   	- Blank line is mandatory.
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4.  Do not end the subject line with a period
5.  Use the imperative mood in the subject line
	- A properly formed Git commit subject line should always be able to complete the following sentence:
	>If applied, this commit will your subject line here
	- Right way: If applied, this commit will refactor subsystem X for readability
	- Wrong way: If applied, this commit will fixed bug with Y
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how