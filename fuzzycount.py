from django.conf import settings
from django.db import connections
from django.db.models import QuerySet, Manager


class FuzzyCountQuerySet(QuerySet):
    def count(self):
        postgres_engines = ("postgis", "postgresql", "django_postgrespool")
        engine = settings.DATABASES[self.db]["ENGINE"].split(".")[-1]
        is_postgres = engine.startswith(postgres_engines)

        if not is_postgres or self.query.where:
            return super(FuzzyCountQuerySet, self).count()
        cursor = connections[self.db].cursor()
        cursor.execute("SELECT reltuples FROM pg_class "
                       "WHERE relname = '%s';" % self.model._meta.db_table)
        return int(cursor.fetchone()[0])


FuzzyCountManager = Manager.from_queryset(FuzzyCountQuerySet)
