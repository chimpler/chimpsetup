import inspect
import sys

from chimpsetup.dependencies import InstallDependenciesCommand, TestDependenciesCommand
from chimpsetup.versions import VersionsCommand


def add_extra_tasks():
    main_module = sys.modules['__main__']
    setup_func = next((obj for name, obj in inspect.getmembers(main_module) if name == 'setup'), None)
    if not setup_func:
        raise Exception('setup not found')

    def proxy_setup(**kwargs):
        default_args = dict([(k, v) for k, v in kwargs.items() if k != 'cmdclass'])
        setup_func(
            cmdclass=dict(
                install_dependencies=InstallDependenciesCommand,
                test_dependencies=TestDependenciesCommand,
                versions=VersionsCommand,
                **kwargs.get('cmdclass', {})
            ),
            **default_args
        )

    setattr(main_module, 'setup', proxy_setup)


add_extra_tasks()
