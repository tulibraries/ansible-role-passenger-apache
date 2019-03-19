Passenger Apache
=========

Installs Phusion Passenger apache module

Requirements
------------

Use `Pipenv` and `.python-version` files to know the required libraries to run this role.


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
