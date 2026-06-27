..
   SPDX-License-Identifier: CC-BY-SA 4.0

   Copyright (C) 2026 David Aderbauer & The Cata-Log Contributors
   Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Configuration
=============

There are two parallel methods to configure your Cata-Log server.

Command-line
------------

Run

.. code-block:: console

    docker run dacid99/cata-log-hub:latest --help

or

.. code-block:: console

    python3 -m cata_log_hub --help

for an overview of the command line interface and the available options.

Environment
-----------

Instead of passing the options via the command line you can set them in the environment as well.

Cata-Log-Hub support both direct enviroment variables as well as a .env file.

.. note::

    Settings via command line always override any environment configurations.
    Environment variables override settings in the .env file.

The names of the environment variables are the names of the corresponding CLI options in UPPER_CAMEL_CASE with prefix *CATA_LOG_*.
So for example, *--request-timeout* becomes *CATA_LOG_REQUEST_TIMEOUT* .

This way of configuring Cata-Log is particularly useful in combination with docker.
`The full docker-compose.yml <https://gitlab.com/cata-log/cata-log-hub/-/blob/main/docker/docker-compose.yml>`_
and `the .env file in the repo <https://gitlab.com/cata-log/cata-log-hub/-/blob/main/.env>`_
list all available options with their defaults.
