"""Contains metadata about the project and its dependencies.
"""

from setuptools import setup, find_packages

setup(
    name='question_cli',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'question-cli=question_cli.cli:run',
        ],
    },
)