import os
import shutil
import sys
import argparse
import tempfile
import pathlib
import shutil
import json
import pathlib
import importlib
import subprocess

import click
from spin import util
from spin.cmds import meson

def _get_nweng_tools(filename):
    filepath = pathlib.Path('tools', filename)
    spec = importlib.util.spec_from_file_location(filename.stem, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@click.command()
@click.option(
    "-j", "--jobs",
    help="Number of parallel tasks to launch",
    type=int
)
@click.option(
    "--clean", is_flag=True,
    help="Clean build directory before build"
)
@click.option(
    "-v", "--verbose", is_flag=True,
    help="Print all build output, even installation"
)
@click.argument("meson_args", nargs=-1)
@click.pass_context
def build(ctx, meson_args, jobs=None, clean=False, verbose=False, quiet=False):
    """🔧 Build package with Meson/ninja and install

    MESON_ARGS are passed through e.g.:

    spin build -- -Dpkg_config_path=/lib64/pkgconfig

    The package is installed to build-install

    By default builds for release, to be able to use a debugger set CFLAGS
    appropriately. For example, for linux use

    CFLAGS="-O0 -g" spin build
    """
    ctx.forward(meson.build)

@click.command()
@click.argument("pytest_args", nargs=-1)
@click.option(
    "-m",
    "markexpr",
    metavar='MARKEXPR',
    default="not slow",
    help="Run tests with the given markers"
)
@click.option(
    "-j",
    "n_jobs",
    metavar='N_JOBS',
    default="1",
    help=("Number of parallel jobs for testing. "
          "Can be set to `auto` to use all cores.")
)
@click.option(
    "--tests", "-t",
    metavar='TESTS',
    help=("""
Which tests to run. Can be a module, function, class, or method:

 \b
 numpy.random
 numpy.random.tests.test_generator_mt19937
 numpy.random.tests.test_generator_mt19937::TestMultivariateHypergeometric
 numpy.random.tests.test_generator_mt19937::TestMultivariateHypergeometric::test_edge_cases
 \b
""")
)
@click.option(
    '--verbose', '-v', is_flag=True, default=False
)
@click.pass_context
def test(ctx, pytest_args, markexpr, n_jobs, tests, verbose):
    """🔧 Run tests

    PYTEST_ARGS are passed through directly to pytest, e.g.:

      spin test -- --pdb

    To run tests on a directory or file:

     \b
     spin test numpy/linalg
     spin test numpy/linalg/tests/test_linalg.py

    To report the durations of the N slowest tests:

      spin test -- --durations=N

    To run tests that match a given pattern:

     \b
     spin test -- -k "geometric"
     spin test -- -k "geometric and not rgeometric"

    By default, spin will run `-m 'not slow'`. To run the full test suite, use
    `spin -m full`

    For more, see `pytest --help`.
    """  # noqa: E501
    if (not pytest_args) and (not tests):
        pytest_args = ('nweng',)

    if '-m' not in pytest_args:
        if markexpr != "full":
            pytest_args = ('-m', markexpr) + pytest_args

    if (n_jobs != "1") and ('-n' not in pytest_args):
        pytest_args = ('-n', str(n_jobs)) + pytest_args

    if tests and not ('--pyargs' in pytest_args):
        pytest_args = ('--pyargs', tests) + pytest_args

    if verbose:
        pytest_args = ('-v',) + pytest_args

    ctx.params['pytest_args'] = pytest_args

    for extra_param in ('markexpr', 'n_jobs', 'tests', 'verbose'):
        del ctx.params[extra_param]
    ctx.forward(meson.test)

@click.command()
@click.option(
    "-b", "--branch",
    metavar='branch',
    default="main",
)
@click.option(
    '--uncommitted',
    is_flag=True,
    default=False,
    required=False,
)
@click.pass_context
def lint(ctx, branch, uncommitted):
    """🔦 Run lint checks on diffs.
    Provide target branch name or `uncommitted` to check changes before committing:

    \b
    Examples:

    \b
    For lint checks of your development brach with `main` or a custom branch:

    \b
    $ spin lint # defaults to main
    $ spin lint --branch custom_branch

    \b
    To check just the uncommitted changes before committing

    \b
    $ spin lint --uncommitted
    """
    try:
        linter = _get_nweng_tools(pathlib.Path('linter.py'))
    except ModuleNotFoundError as e:
        raise click.ClickException(
            f"{e.msg}. Install using linter_requirements.txt"
        )

    linter.DiffLinter(branch).run_lint(uncommitted)

@click.command(context_settings={
    'ignore_unknown_options': True
})
@click.argument("python_args", metavar='', nargs=-1)
@click.pass_context
def python(ctx, python_args):
    """🐍 Launch Python shell with PYTHONPATH set

    OPTIONS are passed through directly to Python, e.g.:

    spin python -c 'import sys; print(sys.path)'
    """
    env = os.environ
    env['PYTHONWARNINGS'] = env.get('PYTHONWARNINGS', 'all')
    ctx.forward(meson.python)


@click.command(context_settings={
    'ignore_unknown_options': True
})
@click.argument("ipython_args", metavar='', nargs=-1)
@click.pass_context
def ipython(ctx, ipython_args):
    """💻 Launch IPython shell with PYTHONPATH set

    OPTIONS are passed through directly to IPython, e.g.:

    spin ipython -i myscript.py
    """
    env = os.environ
    env['PYTHONWARNINGS'] = env.get('PYTHONWARNINGS', 'all')

    ctx.invoke(build)

    ppath = meson._set_pythonpath()

    print(f'💻 Launching IPython with PYTHONPATH="{ppath}"')
    preimport = (r"import numpy as np; "
                 r"print(f'\nPreimported NumPy {np.__version__} as np')")
    util.run(["ipython", "--ignore-cwd",
              f"--TerminalIPythonApp.exec_lines={preimport}"] +
             list(ipython_args))