from setuptools import find_packages, setup

setup(
    name="scraping_project",
    packages=find_packages(exclude=["scraping_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
