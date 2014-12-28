import argparse

from toolbelt import system
from toolbelt import __version__

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', help="Release description", type=str)
args = parser.parse_args()

system.run_command('git tag %s -m "%s" -f' % (__version__, args.message), print_output=True)
system.run_command('git push --tags origin master -f', print_output=True)
system.run_command('python setup.py register -r pypi', print_output=True)
system.run_command('python setup.py sdist upload -r pypi', print_output=True)