Passenger Apache
=========

Installs Phusion Passenger apache module.

Requirements
------------

Use `Pipenv` and `.python-version` files to know the required libraries to run this role.

To run tests:
```
$ pipenv install --dev
  Creating a virtualenv for this project...
  Pipfile: /home/tul08567/Work/src/github.com/tulibraries/ansible-role-passenger-apache/Pipfile
  # etc.
  Installing dependencies from Pipfile.lock (7b941f)...
    🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 64/64 — 00:00:18
  To activate this project's virtualenv, run pipenv shell.
  Alternatively, run a command inside the virtualenv with pipenv run.
$ pipenv run molecule test
  --> Validating schema /home/tul08567/Work/src/github.com/tulibraries/ansible-role-passenger-apache/molecule/default/molecule.yml.
  Validation completed successfully.
  --> Test matrix
  # etc.
  PLAY RECAP *********************************************************************
  localhost                  : ok=2    changed=1    unreachable=0    failed=0
```


Role Variables
--------------
`passenger_package_name`: Defaults to `mod_passenger`, which will install the latest version of passenger available. Specify a release with `mod_passenger-5.3.6`


Dependencies
------------

Expects Apache httpd to be installed


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - ansible-role-passenger-apache

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
