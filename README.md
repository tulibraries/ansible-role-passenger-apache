Passenger Apache
=========

Installs Phusion Passenger apache module

Requirements
------------

Apache2

Role Variables
--------------
`passenger_yum_repos_path`: `/etc/yum.repos.d/passenger.repo`
`passengeryum_repo_download_url`: `https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo`


Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
