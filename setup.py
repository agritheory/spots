from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in spots/__init__.py
from spots import __version__ as version

setup(
	name="spots",
	version=version,
	description="SPOTS",
	author="SPOTS",
	author_email="support@agritheory.dev",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
