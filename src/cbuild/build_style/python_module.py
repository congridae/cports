# FIXME: cross support

from cbuild.core import chroot

def do_build(self):
    self.do("python3", ["setup.py", "build"] + self.make_build_args)

def do_check(self):
    if chroot.enter(
        "python3", ["-c", "import pytest"], capture_out = True,
        ro_root = True, ro_build = True, unshare_all = True
    ).returncode == 0:
        self.do(
            "python3",
            ["-m", "pytest"] + self.make_check_args + [self.make_check_target]
        )
    else:
        self.do(
            "python3",
            ["setup.py", self.make_check_target] + self.make_check_args
        )

def do_install(self):
    self.do(
        "python3", [
            "setup.py", "install", "--prefix=/usr",
            "--root=" + str(self.chroot_destdir)
        ] + self.make_install_args
    )

def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
