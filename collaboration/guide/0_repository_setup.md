# Repository Setup

Before diving into your project make sure your team has all the practical things
in place. This step isn't very hard but everything will go more smoothly if you
take the time to do this correctly at the beginning.

## Setup and Share a Repository

As a team you will choose the name for your team and select someone from your
team to be the repo owner. This person will fork this repository and configure
it for collaboration:

- Public face of your repository
  - Change your
    [repository description](https://stackoverflow.com/questions/7757751/how-do-you-change-a-repository-description-on-github)
  - Add or remove topics from your repository
  - Update your main README with your group name and an initial overview of your
    project. (You can change this as much as you want.)

- Under settings in your repository select:
  - _Issues_
  - _Projects_
  - _Always suggest updating pull request branches_
- Collaboration Settings
  - Require a code review for PRs to `main`/`master`
    ([owanateamachree](https://owanateamachree.medium.com/how-to-protect-the-master-branch-on-github-ab85e9b6b03),
    [github docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/approving-a-pull-request-with-required-reviews))
    - You will need to type `master` into the _Branch name pattern_ input box.
      (or type `main` if you have changed your default branch)
  - Select these settings to protect matching branches:
    - _Require approvals_
    - _Dismiss stale pull request approvals when new commits are pushed_
    - _Require approval of the most recent reviewable push_
    - _Require conversation resolution before merging_
    - _Do not allow bypassing the above settings_

## README

Write the [main README](../../README.md) for your repository! You can always
update it as you learn more about code review and collaboration on GitHub.
