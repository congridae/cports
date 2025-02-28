pkgname = "dehydrated"
pkgver = "0.7.1"
pkgrel = 0
depends = ["bash", "curl", "openssl3"]
pkgdesc = "ACME client implemented as a shell-script"
license = "MIT"
url = "https://github.com/dehydrated-io/dehydrated"
source = f"{url}/releases/download/v{pkgver}/dehydrated-{pkgver}.tar.gz"
sha256 = "4d28a0598230b276b316070ce16be7d9ab984f3bdef482acf0bc24fcdcc0d0b0"


def install(self):
    self.install_bin("dehydrated")
    self.install_license("LICENSE")
