..
   SPDX-License-Identifier: CC-BY-SA 4.0

   Copyright (C) 2026 David Aderbauer & The Cata-Log Contributors
   Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Troubleshooting
===============

This is a curated list of issues that may arise when hosting or using Cata-Log.

What is the default password for my Cata-Log instance?
------------------------------------------------------

Cata-Log has no default password. If you don't set a password yourself, authentication is barred completely.

This is an intentional design choice to allow admins to lock the server down.
Plus default passwords are always a security risk.

Just set your own with the --password cli option or the CATA_LOG_PASSWORD environment variable.

After setting up my Cata-Log instance, I can't access any of the webpages or make API requests.
-----------------------------------------------------------------------------------------------

You have probably not set the hostname of the instance in --allowed-hosts or CATA_LOG_ALLOWED_HOSTS.

I have set an environment variable to configure Cata-Log but it doesn't take effect.
------------------------------------------------------------------------------------

First of all double-check that the variable starts with *CATA_LOG_* and is a UPPER_CAMEL_CASE version of a command-line option.

If that is the case you are probably also setting that command-line option, which overrides the environment setting.

For the docker image the host and port settings are not available as they are needed to correctly expose the Cata-Log server inside the container.
