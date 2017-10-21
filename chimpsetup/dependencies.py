import pip
from setuptools import Command


class DependenciesCommand(Command):
    user_options = [
        ('upgrade', 'u', 'Install dependencies with the --upgrade option'),
    ]

    def __init__(self, dependency_type, dist, **kw):
        Command.__init__(self, dist, **kw)
        self.dependency_type = dependency_type

    def initialize_options(self):
        self.upgrade = 0

    def finalize_options(self):
        pass

    def run(self):
        self.dependencies = self.distribution.tests_require if self.dependency_type == 'test' else self.distribution.install_requires
        upgrade_opt = ['--upgrade'] if self.upgrade else []
        cmd = ['install'] + upgrade_opt + self.dependencies
        pip.main(cmd)


class InstallDependenciesCommand(DependenciesCommand):
    description = "Install test dependencies from setup.py"

    def __init__(self, dist, **kw):
        DependenciesCommand.__init__(self, 'install', dist, **kw)


class TestDependenciesCommand(DependenciesCommand):
    description = "Install dependencies from setup.py"

    def __init__(self, dist, **kw):
        DependenciesCommand.__init__(self, 'test', dist, **kw)
