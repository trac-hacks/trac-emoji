from distutils.core import setup
from setuptools import find_packages

version='0.1'

setup(
    name='TracEmoji',
    long_description='Emoji plugin for trac implementing https://github.com/arvida/emoji-cheat-sheet.com',
    version=version,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    entry_points = """
        [trac.plugins]
        trac_emoji = trac_emoji
    """,
)
