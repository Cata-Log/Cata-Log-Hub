..
   SPDX-License-Identifier: CC-BY-SA 4.0

   Copyright (C) 2026 David Aderbauer & The Cata-Log Contributors
   Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Installation
============

Basic Setup
-----------

There are two main roads to installing Cata-Log:

Docker
^^^^^^

Follow these steps to set up your instance of Cata-Log:

1. Get `the docker-compose.yml file <https://gitlab.com/cata-log/cata-log-hub/-/blob/main/docker/docker-compose.yml>`_ from the git repository.
2. Adapt it to your needs. For details on the environment variables, refer to :doc:`the configuration page <configuration>`.
   Don't forget to set *CATA_LOG_PASSWORD* and *CATA_LOG_ALLOWED_HOSTS*, otherwise you won't be able to access the instance or log in.
3. Deploy the stack any way you wish. Common options are via the command-line

   .. code-block:: console

      docker compose up -d

   or with a container manager like `portainer <https://www.portainer.io/>`_, `dockge <https://dockge.kuma.pet/>`_ or many others.
4. Open *<server_ip>:2424* to check whether the container started successfully.

Bare-Metal
^^^^^^^^^^

Follow these steps to set up your instance of Cata-Log:

1. Install cata_log_hub from PyPI

   .. code-block:: console

      pip install cata-log-hub

   See the following section on :ref:`external databases <External Database>` for details on package extras.

2. Start the server with

   .. code-block:: console

      python3 -m cata_log_hub --password=<your_password> --allowed-hosts=<server_hostname>

   Don't forget the password and allowed_hosts, otherwise you won't be able to access the instance or log in.

3. Open *<server_hostname>:2424* to check whether the container started successfully.

.. important::

    If you want to access Cata-Log from outside your private network, please reverse-proxy.
    The basic HTTP authentication that Cata-Log uses is highly insecure without https!

Further Configuration
---------------------

You can refine the upper basic setup to match your use case.

External Database
^^^^^^^^^^^^^^^^^

Cata-Log uses an internal sqlite3 database by default.
This works fine but has some deficits in terms of concurrency and thread-safety.

If you can, please follow the next steps to use an external full-fledged database server instead.

You can pass the URL of a database either by command-line or environment option to be used instead of the internal sqlite database.

.. note::

    You can use a database that is also used by another application.

    For example if you deploy Cata-Log in the same environment (machine or docker stack) as a shopping-list server,
    you can simply make Cata-Log use the same database container as the main service.
    The two services and their data will not interfere with each other.

Available options are:

- MySQL

  .. code-block:: text

     mysql+pymysql://<db_username>:<db_password>@<database_ip>:<database_port>/cata-log

  Support for MySQL can be installed with the mysql extra

  .. code-block:: console

     pip install cata_log_hub[mysql]

  and is always included in the docker image.

- PostgreSQL

  .. code-block:: text

     postgresql+pg8000://<db_username>:<db_password>@<database_ip>:<database_port>/cata-log

  Support for MySQL can be installed with the mysql extra

  .. code-block:: console

     pip install cata_log_hub[postgres]

  and is always included in the docker image.

.. important::

    Make sure to use the complete protocol with the driver as given in these templates.

You can use the docker-compose files for both setups as reference.

Reverse-Proxy
^^^^^^^^^^^^^

If you intend to use Cata-Log outside of your local network,
it is strongly advised that you reverse-proxy.

(Sub)domain
:::::::::::

This is the standard setup that you probably use for most of your self-hosted applications.

With this setup, Cata-Log will, for example, be available under *https://cata-log.domain.tld*.

Use Nginx, Traeffic or any other webserver of your choice to proxy Cata-Log behind a domain or subdomain.
To ensure correct redirects, set `forward-allow-ips` to the hostname of the proxy.

Custom location
:::::::::::::::

Alternatively, you can attach Cata-Log to an existing proxy host under a custom location.

With this setup, Cata-Log will, for example, be available under *https://sub.domain.tld/cata-log*.

You have to set the `root_path` CLI option (or `CATA_LOG_ROOT_PATH` env variable)
to the path of the custom location for this setup to work correctly.
To ensure correct redirects, set `forward-allow-ips` to the hostname of the proxy.

For Nginx an exemplary config is

.. code-block:: text

    location /cata-log/ {
        proxy_pass http://<server_ip>:2424;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

In this example, `root_path` must be set to */cata-log*.

For more details, see `the fastapi docs on this subject <https://fastapi.tiangolo.com/advanced/behind-a-proxy/#redirects-with-https>`_.

Settings
^^^^^^^^

Your instance can be configured in many individual settings.

Refer to :doc:`the configuration page <configuration>` for all details.
