from distutils.version import LooseVersion

from django.conf import settings
from django.db import connections
from django.db.models import QuerySet, Manager
import django


DJANGO_VERSION_GTE_19 = LooseVersion(django.get_version()) \
                        >= LooseVersion('1.9')


class FuzzyCountQuerySet(QuerySet):
    def count(self):
        postgres_engines = ("postgis", "postgresql", "django_postgrespool")
        engine = settings.DATABASES[self.db]["ENGINE"].split(".")[-1]
        is_postgres = engine.startswith(postgres_engines)

        # In Django 1.9 the query.having property was removed and the
        # query.where property will be truthy if either where or having
        # clauses are present. In earlier versions these were two separate
        # properties query.where and query.having
        if DJANGO_VERSION_GTE_19:
            is_filtered = self.query.where
        else:
            is_filtered = self.query.where or self.query.having
        if not is_postgres or is_filtered:
            return super(FuzzyCountQuerySet, self).count()
        cursor = connections[self.db].cursor()
        cursor.execute("SELECT reltuples FROM pg_class "
                       "WHERE relname = '%s';" % self.model._meta.db_table)
        return int(cursor.fetchone()[0])


FuzzyCountManager = Manager.from_queryset(FuzzyCountQuerySet)
