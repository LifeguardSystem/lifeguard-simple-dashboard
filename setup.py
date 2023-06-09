from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lifeguard-simple-dashboard",
    version="1.0.0",
    url="https://github.com/LifeguardSystem/lifeguard-simple-dashboard",
    author="Diego Rubin",
    author_email="contact@diegorubin.dev",
    license="GPL2",
    scripts=[],
    include_package_data=True,
    description="Implementation of a simple Lifeguard Dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["lifeguard"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Monitoring",
    ],
    packages=find_packages(),
)
