# skerna-template

https://skerna.gitlab.io/homepage/

## About

Project description here.

[API Documentation](https://skerna.gitlab.io/homepage/)

## [Change log](CHANGELOG.md)

### Tools

In our project ecosystem, we have strategically incorporated a suite of robust and essential tools designed to
streamline our development process and enhance the overall quality and efficiency of our work. These tools have been
carefully selected to address critical aspects of our development lifecycle, ensuring a seamless and optimized workflow.

## How use
if you use vscode you can open in vscode with devcontainer :D 
only one command, and everything will be configurated 
``` bash
   yarn install
```
when you call yarn install post scripts it will happen:
2) npm packages will be installed
   3) Semantic Commit
   4) Pre commits
1) prepare npm will be trigger it'l install git hooks
3) poetry python packages will be installed
4) python virtual env inside project




#### Tools
- Python 3.10.0 // [PYENV](https://github.com/pyenv/pyenv) is recommended for manager python versions
- Node v18.15.0 + // [NVM](https://github.com/nvm-sh/nvm) is recommended for manage node
- [Husky precommits](https://typicode.github.io/husky/) 
- [Semantic Commits](https://www.conventionalcommits.org/en/v1.0.0/) 
- [Commitizen](http://commitizen.github.io/cz-cli/)
- [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)
- [Poetry Support](https://python-poetry.org)
- [Ruff linters](https://github.com/astral-sh/ruff) 
  - [autoflake](https://pypi.org/project/autoflake/)
  - [eradicate](https://pypi.org/project/eradicate/)
  - [flake8-2020](https://pypi.org/project/flake8-2020/)
  - [flake8-annotations](https://pypi.org/project/flake8-annotations/)
  - [flake8-async](https://pypi.org/project/flake8-async)
  - [flake8-bandit](https://pypi.org/project/flake8-bandit/) ([#1646](https://github.com/astral-sh/ruff/issues/1646))
  - [flake8-blind-except](https://pypi.org/project/flake8-blind-except/)
  - [flake8-boolean-trap](https://pypi.org/project/flake8-boolean-trap/)
  - [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
  - [flake8-builtins](https://pypi.org/project/flake8-builtins/)
  - [flake8-commas](https://pypi.org/project/flake8-commas/)
  - [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/)
  - [flake8-copyright](https://pypi.org/project/flake8-copyright/)
  - [flake8-datetimez](https://pypi.org/project/flake8-datetimez/)
  - [flake8-debugger](https://pypi.org/project/flake8-debugger/)
  - [flake8-django](https://pypi.org/project/flake8-django/)
  - [flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
  - [flake8-eradicate](https://pypi.org/project/flake8-eradicate/)
  - [flake8-errmsg](https://pypi.org/project/flake8-errmsg/)
  - [flake8-executable](https://pypi.org/project/flake8-executable/)
  - [flake8-future-annotations](https://pypi.org/project/flake8-future-annotations/)
  - [flake8-gettext](https://pypi.org/project/flake8-gettext/)
  - [flake8-implicit-str-concat](https://pypi.org/project/flake8-implicit-str-concat/)
  - [flake8-import-conventions](https://github.com/joaopalmeiro/flake8-import-conventions)
  - [flake8-logging-format](https://pypi.org/project/flake8-logging-format/)
  - [flake8-no-pep420](https://pypi.org/project/flake8-no-pep420)
  - [flake8-pie](https://pypi.org/project/flake8-pie/)
  - [flake8-print](https://pypi.org/project/flake8-print/)
  - [flake8-pyi](https://pypi.org/project/flake8-pyi/)
  - [flake8-pytest-style](https://pypi.org/project/flake8-pytest-style/)
  - [flake8-quotes](https://pypi.org/project/flake8-quotes/)
  - [flake8-raise](https://pypi.org/project/flake8-raise/)
  - [flake8-return](https://pypi.org/project/flake8-return/)
  - [flake8-self](https://pypi.org/project/flake8-self/)
  - [flake8-simplify](https://pypi.org/project/flake8-simplify/)
  - [flake8-slots](https://pypi.org/project/flake8-slots/)
  - [flake8-super](https://pypi.org/project/flake8-super/)
  - [flake8-tidy-imports](https://pypi.org/project/flake8-tidy-imports/)
  - [flake8-todos](https://pypi.org/project/flake8-todos/)
  - [flake8-type-checking](https://pypi.org/project/flake8-type-checking/)
  - [flake8-use-pathlib](https://pypi.org/project/flake8-use-pathlib/)
  - [flynt](https://pypi.org/project/flynt/) ([#2102](https://github.com/astral-sh/ruff/issues/2102))
  - [isort](https://pypi.org/project/isort/)
  - [mccabe](https://pypi.org/project/mccabe/)
  - [pandas-vet](https://pypi.org/project/pandas-vet/)
  - [pep8-naming](https://pypi.org/project/pep8-naming/)
  - [pydocstyle](https://pypi.org/project/pydocstyle/)
  - [pygrep-hooks](https://github.com/pre-commit/pygrep-hooks)
  - [pylint-airflow](https://pypi.org/project/pylint-airflow/)
  - [pyupgrade](https://pypi.org/project/pyupgrade/)
  - [tryceratops](https://pypi.org/project/tryceratops/)
  - [yesqa](https://pypi.org/project/yesqa/)



#### Monorepo Tools NX Initial Support

Our toolkit encompasses cutting-edge monorepo tools with added NX initial support, empowering us to efficiently manage
multiple projects within a single repository. This approach fosters modularity, code reuse, and simplified dependency
management, facilitating collaborative development and effective code sharing.

#### Semantic Commits

We adhere to the best practices of semantic commits, a structured approach to our version control messages. By
categorizing our commit messages with clear and standardized prefixes, we ensure consistency and precision in our
communication, enabling better understanding and tracking of changes.

#### Semantic Release

Automating our version release process, Semantic Release empowers us to effortlessly generate accurate version numbers
and changelogs based on our semantic commits. This tool enables us to focus on creating impactful code while ensuring
that our releases are properly documented and communicated.

#### Changelogs

Changelogs play a pivotal role in transparently communicating the evolution of our software. With our integrated
changelog tools, we can automatically generate comprehensive and organized changelogs, making it easier for stakeholders
to grasp the significance of each release.

#### Linters

Our toolkit includes advanced linters that perform rigorous code analysis, enforcing coding standards, identifying
potential issues, and enhancing code quality. By incorporating linters into our workflow, we maintain a high level of
code consistency and readability.

#### Test

Testing is fundamental to our development process, and our integrated testing tools provide us with a robust framework
to ensure the reliability and stability of our codebase. With automated testing suites, we can confidently identify and
rectify issues early in the development cycle, guaranteeing the delivery of robust and dependable software.

Incorporating these indispensable tools into our development arsenal showcases our commitment to delivering exceptional
software solutions while optimizing collaboration, code quality, and release management. Each facet of our toolkit
contributes to a holistic approach to software development, allowing us to focus on innovation and excellence while the
tools handle the intricacies of our development lifecycle.
