from datasets.nap import batch as napbatch
from datasets import nap
from batch.tests.test import TaskTestCase

NAP = 'diva/nap'


class ImportNapTest(TaskTestCase):
    def task(self):
        return napbatch.ImportNapTask(NAP)

    def test_import(self):
        self.run_task()

        imported = nap.models.Peilmerk.objects.all()
        self.assertEqual(len(imported), 639)

        a = nap.models.Peilmerk.objects.get(pk='10480009')
        self.assertEqual(a.omschrijving, 'Spuistraat 94')
