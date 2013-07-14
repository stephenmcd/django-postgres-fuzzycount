
from django.conf import settings
from django.db import connections
from django.db.models.query import QuerySet

from model_utils.managers import PassThroughManager


class FuzzyCountQuerySet(QuerySet):

    def count(self):
        postgres_engines = ("postgis", "postgresql", "django_postgrespool")
        engine = settings.DATABASES[self.db]["ENGINE"].split(".")[-1]
        is_postgres = engine.startswith(postgres_engines)
        is_filtered = self.query.where or self.query.having
        if not is_postgres or is_filtered:
            return super(FuzzyCountQuerySet, self).count()
        cursor = connections[self.db].cursor()
        cursor.execute("SELECT reltuples FROM pg_class "
                       "WHERE relname = '%s';" % self.model._meta.db_table)
        return int(cursor.fetchone()[0])


FuzzyCountManager = PassThroughManager.for_queryset_class(FuzzyCountQuerySet)
