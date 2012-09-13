"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.db import models

from south.db import db

from models import X, Y


class SimpleTest(TestCase):
    def test_basic_addition(self):
        # create field
        f = models.ManyToManyField(to=X, related_name='bar')
        f.contribute_to_class(Y, 'x')

        # create table
        field = Y._meta.get_field_by_name('x')[0]
        through = field.rel.through

        fields = tuple((field.name, field) for field in through._meta.fields)

        db.create_table(through._meta.db_table, fields)
        db.create_unique(through._meta.db_table,
            ['%s_id' % name for name, f in fields
                if isinstance(f, models.ForeignKey)])


        x = X(name='foo')
        x.save()
        y = Y()
        y.save()
        y.x.add(x)

        print y.x.all()
