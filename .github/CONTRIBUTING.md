<!--
Marked Style: GitHub
# TODO
    * How to contribute changes
        * Base work off develop
        * Sematic Versioning
            * https://semver.org/
        * Linting
        * Interface changes should include updates to `yadm.1`
        * Commits
            * Commit messages (Tim Pope style)
                * https://chris.beams.io/posts/git-commit/
            * Atomic commits
                * https://www.google.com/search?q=atomic+commits
            * Signed Commits
                * https://help.github.com/en/articles/signing-commits
    * Packaging
        * "Watch releases"
-->

# Introduction

Thank you for considering contributing to **yadm**.
I develop this project in my limited spare time, so help is very appreciated.

All contributors must follow our [Code of Conduct][conduct]. Please make sure
you are welcoming and friendly during your interactions, and report any
unacceptable behavior to <yadm@yadm.io>.

Contributions can take may forms, and often don’t require writing code—maybe
something could be documented more clearly, maybe a feature could be more
helpful, maybe installation could be easier. Help is welcome in any of these
areas.

To contribute, you can:

* Report [bugs](#reporting-a-bug)
* Request [features/enhancements](#suggesting-a-feature-or-enhancement)
* Contribute changes to [code, tests](#contributing-code), and [documentation](#improving-documentation)
* Maintain installation [packages](#maintaining-packages)
* Help others users by [answering support questions](#answering-support-questions)

# Reporting a bug

Notice something amiss? You’re already helping by reporting the problem! Bugs
are tracked using GitHub issues. Here are some steps you can take to help
problems get fixed quickly and effectively:

### Before submitting an issue

Please take a quick look to see whether the problem has been reported already
(there’s a list of [open issues][open-issues]). You can try the search function
with some related terms for a cursory check. If you do find a previous report,
please add a comment there instead of opening a new issue.

### Security issues

If you have found a security vulnerability, do **NOT** open an issue.

Any security issues should be emailed directly to <yadm@yadm.io>. In order to
determine whether you are dealing with a security issue, ask yourself these two
questions:

* Can I access something that's not mine, or something I shouldn't have access to?
* Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably
dealing with a security issue.

### Submitting a (great) bug report

Choose the "[Bug report][new-bug]" issue type.

Pick a descriptive title that clearly identifies the issue.

Describe the steps that led to the problem so that we can go through the same sequence.
A clear set of steps to reproduce the problem is key to fixing an issue.
If possible, attach a [`script.gz`](#attaching-a-scriptgz) to the bug report.

Describe what you had expected and how that differed from what happened, and possibly, why.

Include the version numbers of your operating system, of **yadm**, and of Git.

### Attaching a script.gz
Consider trying to reproduce the bug inside a docker container using the
[yadm/testbed][testbed] docker image.
Doing so will greatly increase the likelihood of the problem being fixed.

The easiest way to start this container, is to clone the [TheLocehiliosan/yadm
repo][yadm-repo], and use the `scripthost` make target. _(You will need `make`
and `docker` installed.)_

For example:

```text
$ git clone https://github.com/TheLocehiliosan/yadm.git
$ cd yadm
$ make scripthost version=1.12.0
Starting scripthost version="1.12.0" (recording script)
root@scripthost:~# ### run commands which
root@scripthost:~# ### demonstrate the problem
root@scripthost:~# ### a succinct set of commands is best
root@scripthost:~# exit
logout

Script saved to script.gz
$
```

A `script.gz` like this can be useful to developers to make a repeatable test
for the problem. You can attach the `script.gz` file to an issue.
Look [here][attach-help] for help with [attaching a file][attach-help].

# Suggesting a feature or enhancement

Have an idea for an improvement? Creating a feature request is a good way to
communicate it.

### Before submitting an issue

Please take a quick look to see whether your idea has been suggested already
(there’s a list of [open issues][open-issues]). You can try the search function
with some related terms for a cursory check. If you do find a previous feature
request, please add a comment there instead of opening a new issue.

### Submitting a (great) feature request

Choose the "[Feature request][new-feature]" issue type.

Summarize your idea with a clear title.

Describe your suggestion in as much detail as possible.

Explain alternatives you've considered.

# Contributing code

Wow, thank you for considering making a contribution of code!

### Before you begin

Please take a quick look to see whether a similar change is already being worked
on. A similar pull request may already exist. If the change is related to an
issue, look to see if that issue has an assignee.

Consider reaching out before you start working. It's possible developers may
have some ideas and code lying around, and might be able to give you a head
start.

[Creating a hook][hooks-help] is an easy way to begin adding features to an
already existing **yadm** operation. If the hook works well, it could be the
basis of a **yadm** feature addition.

### Design principles

**yadm** was created with a few core design principles in mind. Please adhere to
these principles when making changes.

* **Single repository**
    * **yadm** is designed to maintain dotfiles in a single repository.

* **Very few dependencies**
    * **yadm** should be as portable as possible. This is one of the main
      reasons it has only two dependencies (Bash and Git). Features using other
      dependencies should gracefully downgrade instead of breaking. For example,
      encryption requires GnuPG installed, and displays that information if it
      is not.

* **Sparse configuration**
    * **yadm** should require very little configuration, and come with sensible
      defaults. Changes requiring users to define meta-data for all of their
      dotfiles will not be accepted.

* **Maintain dotfiles in place**
    * The default treatment for tracked data should be to allow it to remain a
      file, in the location it is normally kept.

* **Leverage Git**
    * Stay out of the way and let Git do what it’s good at. Git has a deep and
      rich set of features for just about every use case. Staying hands off for
      almost all Git operations will make **yadm** more flexible and
      future-proof.

### Repository branches and tags

* `master`
    * This branch will always represent the latest release of **yadm**.
* `#.#.#` _(tags)_
    * Every release of **yadm** will have a commit tagged with the version number.
* `develop`
    * This branch should be used for the basis of every change. As changes are
      accepted, they will be merged into `develop`.
* `release/*`
    * These are ephemeral branches used to prepare new releases.
* `hotfix/*`
    * These are ephemeral branches used to prepare a patch release, which only
      includes bug fixes.
* `gh-pages`
    * This branch contains the yadm.io website source.
* `dev-pages`
    * This branch should be used for the basis of every website change. As
      changes are accepted, they will be merged into dev-pages.
* `netlify/*`
    * These branches deploy configurations to Netlify websites. Currently this
      is only used to drive redirections for
      [bootstrap.yadm.io](https://bootstrap.yadm.io/).

### GitHub workflow

1. Fork the [yadm repository][yadm-repo] on GitHub.

2. Clone your fork locally.

    ```text
    $ git clone <url-to-your-fork>
    ```

3. Add the official repository (`upstream`) as a remote repository.

    ```text
    $ git remote add upstream https://github.com/TheLocehiliosan/yadm.git
    ```

4. Verify you can run the test harness. _(This will require dependencies, `make`, `docker`, and `docker-compose`)_.

    ```text
    $ make test
    ```

5. Create a feature branch, based off the `develop` branch.

    ```text
    $ git checkout -b <name-of-feature-branch> upstream/develop
    ```

6. Add changes to your feature branch.

7. If your changes take a few days, be sure to occasionally pull the latest
changes from upstream, to ensure that your local branch is up-to-date.

    ```text
    $ git pull --rebase upstream develop
    ```

8. When your work is done, push your local branch to your fork.

    ```text
    $ git push origin <name-of-feature-branch>
    ```

9. [Create a pull request][pr-help] on GitHub.

# Improving documentation

Wow, thank you for considering making a documentation improvements!

* Man page

* Website

# Maintaining packages

# Answering support questions

Are you an experienced **yadm** user, with an advanced knowledge of Git? Your
expertise could be useful to someone else who is starting out or struggling with
a problem. Consider reviewing the list of [open support questions][questions] to
see if you can help.

[attach-help]: https://help.github.com/en/articles/file-attachments-on-issues-and-pull-requests
[conduct]: https://link-to-conduct/TODO.md
[contrib-hooks]: https://github.com/TheLocehiliosan/yadm/tree/master/contrib/hooks
[hooks-help]: https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#hooks
[new-bug]: https://github.com/TheLocehiliosan/yadm/issues/new?template=BUG_REPORT.md
[new-feature]: https://github.com/TheLocehiliosan/yadm/issues/new?template=FEATURE_REQUEST.md
[open-issues]: https://github.com/TheLocehiliosan/yadm/issues
[pr-help]: https://help.github.com/en/articles/creating-a-pull-request-from-a-fork
[questions]: https://github.com/TheLocehiliosan/yadm/labels/question
[testbed]: https://hub.docker.com/r/yadm/testbed
[yadm-repo]: https://github.com/TheLocehiliosan/yadm
