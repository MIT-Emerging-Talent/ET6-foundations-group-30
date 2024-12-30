# Constraints

## External Constraints

**These factors outside our control influence how we work on this project.**

### Platform Requirements

- Problems must be selected from the workshop's exercises, CodeWars, LeetCode, or
similar coding platforms.
- Solutions must comply with the workshop's requirements (e.g., unit tests, documentation,
 and clear variable names).

### Deadlines

- Projects must be completed according to the timeline set by the
MIT Emerging Talent program.
- Each member must solve and review problems within the agreed-upon timeframes.

### Tools and Resources

- GitHub must be used for version control, communication, and documentation.
- The team must rely on publicly available resources (e.g., online tutorials
and documentation) to enhance learning.

## Internal Constraints: Voluntary

These are self-imposed rules or boundaries designed to improve collaboration and
learning outcomes.

### Documentation Standards

- All code must include meaningful comments explaining the logic.
- Problem solutions must include documentation with:
  - Problem description.
  - Approach and thought process.
  - Test cases used.

### Communication Protocols

- Use GitHub Issues to discuss problems and tasks.
- At least one other member must review pull requests before merging.
- Constructive feedback is required for all reviews.

### Collaborative Learning

- Each member must share insights or challenges they faced during problem-solving
 to help others learn.
- Regular check-ins (via GitHub comments or virtual meetings) to ensure alignment.

## New Internal Constraints: Voluntary

These are new rules designed to improve the workflow and mitigate issues we've
encountered recently.

### Pull Request and Branching Practices

- **Pull Requests**: Each template file must be worked on in a separate branch and
added to the TODO list of the project board.
- **Branch Management**: When creating a new branch, ensure it is synchronized and
updated with the main branch using the following commands:
  - `git fetch` to fetch updates.
  - `git merge main` to merge the latest main branch changes into the current branch.
- **Selective `git add`**: Only add files on which changes have been made.
**Do not use `git add .`**. This ensures only relevant changes are committed.
- **Template File Changes**: For all template file modifications, work exclusively
in the `update_template_files` branch.
Create an issue for any changes you wish to make, and only submit a pull request
if you plan to merge the changes into the main file.
- **Branch Closure**: Once a new branch is created and used, the previous branches
will not be used further. Always start from the latest main branch or an appropriate
updated branch.
- **Pull Request Review**: Pull requests must be reviewed promptly upon submission
to avoid delays and conflicts. Reviews should be completed as soon as possible to
ensure efficient merging.
