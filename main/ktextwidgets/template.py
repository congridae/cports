pkgname = "ktextwidgets"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qttools-devel",
    "sonnet-devel",
]
pkgdesc = "KDE Text editing widgets"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/ktextwidgets/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktextwidgets-{pkgver}.tar.xz"
sha256 = "4db67be70da68e3fd2c2a9d3359dcfb9b11eb82a34f2b88d3e6ed08e358ab073"
hardening = ["vis"]


@subpackage("ktextwidgets-devel")
def _(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel()
