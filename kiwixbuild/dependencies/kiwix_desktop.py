from .base import (
    Dependency,
    GitClone,
    QMakeBuilder)
from kiwixbuild._global import neutralEnv

class KiwixDesktop(Dependency):
    name = "kiwix-desktop"

    class Source(GitClone):
        git_remote = "https://github.com/kiwix/kiwix-desktop.git"
        git_dir = "kiwix-desktop"

    class Builder(QMakeBuilder):
        dependencies = ['qt', 'qtwebengine', 'kiwix-lib']

        @classmethod
        def get_dependencies(self, platformInfo, allDeps):
            if neutralEnv('distname') == 'Windows':
                return ['kiwix-lib']
            return cls.dependencies
        
        @property
        def configure_option(self):
            options = ["PREFIX={}".format(self.buildEnv.install_dir)]
            if self.buildEnv.platformInfo.static:
                options.append('"CONFIG+=static"')
            return " ".join(options)
