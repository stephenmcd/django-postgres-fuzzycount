Created by `Stephen McDonald <http://twitter.com/stephen_mcd>`_

Introduction
============

Up until PostgreSQL 9.2, ``COUNT`` queries generally required scanning
every row in a database table. With millions of rows, this can become
quite slow. One work-around for this is to query statistics in
PostgreSQL for an approximate row count, which in many cases is an
acceptable trade-off.

Given a table called ``bigdata``, the following query will return an
approximate row count::

    SELECT reltuples FROM pg_class WHERE relname = 'bigdata';

You can read more information about `slow COUNT queries in PostgreSQL`_
in the PostgreSQL wiki.

What ``django-postgres-fuzzycount`` provides is a way of using this
approach directly in your Django model managers. It was originally
built for displaying statistics in the `kouio RSS reader`_, a popular alternative to Google Reader, that acquired over 5 million news articles
in its database during the first week of its launch.

Installation
============

The easiest way to install ``django-postgres-fuzzycount`` is directly
from PyPi using `pip`_ by running the following command::

    $ pip install -U django-postgres-fuzzycount

Otherwise you can download and install it directly from source::

    $ python setup.py install

Usage
=====

By using the ``fuzzycount.FuzzyCountManager`` on your Django models,
its ``count()`` method will return an approximate value when querying
PostgreSQL tables without any ``WHERE`` OR ``HAVING`` clauses::

    from django.db import models
    from fuzzycount import FuzzyCountManager

    class BigData(models.Model):

        big = models.BooleanField(default=True)
        data = models.TextField()

        objects = FuzzyCountManager()

    BigData.objects.count()  # Uses fuzzycount
    BigData.objects.filter(id__gt=9000).count()  # Doesn't use fuzzycount

The ``fuzzycount.FuzzyCountManager`` also checks the database engine
being used, and only applies the approximate count query when using
PostgreSQL, so other database backends can be used and will behave as
usual (for varying definitions of `usual`, depending on the database :-).

Inspiration
===========

  * `postgres_loose_table_counts`_, a Ruby gem providing the same
    approach for Rails
  * This `Django snippet`_, which bakes the approach into the admin

.. _`slow COUNT queries in PostgreSQL`: http://wiki.postgresql.org/wiki/Slow_Counting
.. _`kouio RSS reader`: https://kouio.com
.. _`pip`: http://www.pip-installer.org/
.. _`postgres_loose_table_counts`: https://github.com/goodfilms/postgres_loose_table_counts
.. _`Django snippet`: http://djangosnippets.org/snippets/2855/
