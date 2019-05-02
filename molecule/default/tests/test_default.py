import os

# import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_apache(host):
    if host.system_info.distribution == "ubuntu":
        package = host.package("apache2")
    elif host.system_info.distribution == "centos":
        package = host.package("httpd")
    else:
        package = host.package("apache2")

    assert package.is_installed


def test_svc(host):
    if host.system_info.distribution == "ubuntu":
        service = host.service("apache2")
    elif host.system_info.distribution == "centos":
        service = host.service("httpd")
    else:
        service = host.service("apache2")

    assert service.is_running
    assert service.is_enabled


# @pytest.mark.parametrize('pkg', [
#     '1c-enterprise83-common',
#     '1c-enterprise83-common-nls',
#     '1c-enterprise83-server',
#     '1c-enterprise83-server-nls',
#     '1c-enterprise83-ws',
#     '1c-enterprise83-ws-nls'
#     ])
# def test_pkg(host, pkg):
#     package = host.package(pkg)
#     assert package.is_installed

# '1c-enterprise83-common',
# '1c-enterprise83-server'


# package name centos
# 1C_Enterprise83-server-8.3.13-1644.x86_64
# 1C_Enterprise83-ws-nls-8.3.13-1644.x86_64
# 1C_Enterprise83-common-nls-8.3.13-1644.x86_64
# 1C_Enterprise83-common-8.3.13-1644.x86_64
# 1C_Enterprise83-ws-8.3.13-1644.x86_64
# 1C_Enterprise83-server-nls-8.3.13-1644.x86_64
