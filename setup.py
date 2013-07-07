
from setuptools import setup, find_packages


setup(
    name = "django-postgres-fuzzycount",
    version = "0.1.1",
    author = "Stephen McDonald",
    author_email = "stephen.mc@gmail.com",
    description = ("A Django model manager providing fast / fuzzy counts "
                   "for PostgreSQL database tables."),
    long_description = open("README.rst").read(),
    url = "http://github.com/kouio/django-postgres-fuzzycount",
    zip_safe = False,
    include_package_data = True,
    packages = find_packages(),
    install_requires = [
        "sphinx-me >= 0.1.2",
        "django >= 1.4",
        "django-model-utils==1.4.0",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ]
)
