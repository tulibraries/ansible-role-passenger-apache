import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_passenger_config_present(host):
    f = host.file("/etc/httpd/conf.modules.d/00-passenger.conf")
    assert f.exists
    assert f.contains("LoadModule passenger_module")
