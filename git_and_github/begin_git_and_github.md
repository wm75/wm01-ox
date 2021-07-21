# Get started with git and github

## Clarifications

`git` is a command-line tool for version-controlled and distributed development.

*github* is a web-based platform for collaborative development with `git`.

=> You can use `git` without *github*, but not *github* without `git`.

There are many similar web services/platforms like *github*, but *github* is
currently the most widely used such platform by far. In other words, this is
where most collaboration happens.


## Introduction to git

### Installation

First, lets install `git` and perform initial minimal configuration.

Use the instructions provided as part of the *github* documentation for this:

https://docs.github.com/en/get-started/quickstart/set-up-git#setting-up-git

For the moment just follow the three steps - installation, username and email
configuration.

### Using git for local version-control

Lets illustrate basic functionality of `git` with a toy example: a small piece
of code for generating random biological sequences. Get an initial Python
script from [here](./random_seq.py) and store this file in an otherwise empty
folder on your local system.

Open a terminal/console window, `cd` into the folder with the file, and run the
script with:

`python random_seq.py`

Oh, of course! You would need to specify the desired sequence length. Try again
with:

`python random_seq.py 20`

Ah, better!



