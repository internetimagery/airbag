
import shutil
import unittest
import tempfile
import os.path

from clean_transaction import Transaction
import clean_transaction.actions.IO


class TestIOFile(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_file_create(self):
        path = os.path.join(self.tempdir, "file1.txt")
        with Transaction() as action:
            action.IO.file.create(path, "someinfo")
        self.assertTrue(os.path.isfile(path))

        path = os.path.join(self.tempdir, "file2.txt")
        with self.assertRaises(RuntimeError):
            with Transaction() as action:
                action.IO.file.create(path, "someinfo")
                raise RuntimeError()
        self.assertFalse(os.path.isfile(path))

class TestIODir(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_file_create(self):
        path = os.path.join(self.tempdir, "dir1")
        with Transaction() as action:
            action.IO.dir.create(path)
        self.assertTrue(os.path.isdir(path))

        path = os.path.join(self.tempdir, "dir2")
        with self.assertRaises(RuntimeError):
            with Transaction() as action:
                action.IO.dir.create(path)
                raise RuntimeError()
        self.assertFalse(os.path.exists(path))


if __name__ == '__main__':
    unittest.main()