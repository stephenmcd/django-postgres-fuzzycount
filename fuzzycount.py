
from django.conf import settings
from django.db import connections
from django.db.models.query import QuerySet

from model_utils.managers import PassThroughManager


class FuzzyCountQuerySet(QuerySet):

    def count(self):
        is_postgresql = "postgresql" in settings.DATABASES[self.db]["ENGINE"]
        is_filtered = self.query.where or self.query.having
        if not is_postgresql or is_filtered:
            return super(FuzzyCountQuerySet, self).count()
        cursor = connections[self.db].cursor()
        cursor.execute("SELECT reltuples FROM pg_class "
                       "WHERE relname = '%s';" % self.model._meta.db_table)
        return int(cursor.fetchone()[0])


FuzzyCountManager = PassThroughManager.for_queryset_class(FuzzyCountQuerySet)
