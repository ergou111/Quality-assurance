import coverage
import unittest

cov = coverage.coverage()
cov.start()

suite = unittest.defaultTestLoader.discover("./", "test_solution.py")
unittest.TextTestRunner().run(suite)

cov.stop()
cov.save()

cov.report()
cov.html_report(directory='coverage-report')
