import nox


@nox.session(python=["3.5", "3.6", "3.7"])
def tests(session):
    """Run the unit test suite."""
    session.install("pytest", "pytest-cov")
    session.install("-e", ".")

    # Run py.test against the unit tests.
    session.run(
            "pytest", "--quiet", "--cov=mortgage", "--cov-branch", "--cov-report=xml", "tests", *session.posargs)


@nox.session
def cover(session):
    """Coverage analysis."""
    session.install("coverage")
    fail_under = "--fail-under=85"
    session.run("coverage", "report", fail_under, "--show-missing")
    session.run("coverage", "erase")


@nox.session(python="3.7")
def docs(session):
    """Build the documentation."""
    session.run("rm", "-rf", "docs/_build", external=True)
    session.install("-e", ".[develop]")
    session.cd("docs")
    sphinx_args = ["-b", "html", "-W", "-d", "_build/doctrees", ".", "_build/html"]

    if "serve" not in session.posargs:
        sphinx_cmd = "sphinx-build"
    else:
        sphinx_cmd = "sphinx-autobuild"
        sphinx_args.insert(0, "--open-browser")

    session.run("make", "doctest")
    session.run(sphinx_cmd, *sphinx_args)
