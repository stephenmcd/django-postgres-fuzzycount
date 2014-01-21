from setuptools import setup


setup(
    name = "django-postgres-fuzzycount",
    version = "0.1.6",
    author = "Stephen McDonald",
    author_email = "stephen.mc@gmail.com",
    description = ("A Django model manager providing fast / fuzzy counts "
                   "for PostgreSQL database tables."),
    long_description = open("README.rst").read(),
    url = "http://github.com/stephenmcd/django-postgres-fuzzycount",
    zip_safe = False,
    py_modules=["fuzzycount",],
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
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ]
)
