# Cata-Log Hub

The central hub for digital flyers.

If you can check at least two of the following, this project is for you:

- [ ] You like to shop items that are on offer.
- [ ] You like to check what's on offer before you go to the store.
- [ ] You care about privacy.
- [ ] You want to use open-source software.

## What does Cata-Log do?

Cata-Log-Hub lets you cache and access the digital flyer for your favorite stores in a single interface.

Select from a list of flyer providers to routinely cache them.
You can then read them

- in a webapp
- via an OPDS catalog
- with an extensive API

Cata-Log also provides client libraries to make development and integration in third-party apps easy!

## Project Status

*BETA*

- The backend is stable.

- The provisional webui still needs some polishing.

- I have added the most relevant german flyer providers,
  other regions must be contributed
  as I am not familiar with the stores or the languages used.

## Roadmap

- Setup client libraries and ship them
- Fixes and consolidation

See [the TODO list for future ideas](TODO.md).

## Documentation

The full documentation is available on [ReadTheDocs][readthedocs].

It gives full context and details on installation and configuration
as well as helpful guides and resources for contributing.

## Installation

The Cata-Log-Hub server is intended to be run
either with the container image provided at [dockerhub][dockerhub]
or bare-metal with the [python-package][pypi].

Cata-Log-Hub comes with a sqlite3 database by default,
but you can also choose to use mysql or postgres instead.

### Docker

Use *docker compose* using [the compose file](docker/docker-compose.minimal.yml)
or an equivalent *docker run* command.

### Podman

Do the same thing as above, just using *podman* instead of *docker*.

### Kubernetes

You can use a tool like [kompose](https://kompose.io)
to translate [the docker compose file](docker/docker-compose.minimal.yml)
to a kubernetes cluster configuration.

### Bare-Metal

Install the cata-log python package. It requires at least Python version 3.14 .

```console
pip install cata-log-hub
```

and start the server

```console
python3 -m cata_log_hub --password=<password>
```

You can get an overview over all CLI options with

```console
python3 -m cata_log_hub --help
```

Configuration is done with the command-line options,
environment variables or .env file.


### Agentic installation

If you want an agent to install Cata-Log-Hub for you,
point it to [the install.md file](install.md), e.g.

```bash
  curl -fsSL https://github.com/cata-log/cata-log-hub/blob/master/install.md | claude
```

## Contributing

THIS PROJECT LIVES FROM YOUR CONTRIBUTIONS!

If there is a provider class you are missing, give implementing it a try.
The quickstart and guide for implementing a provider class are in the documentation.

Thank you to [everybody who helped with advancing this project](CONTRIBUTORS.md)
and [who helped with translation](TRANSLATORS.rst)!

## Legal

This software is entirely human-made. Every single line of code is hand-written.
AI was only used for research and bouncing ideas.

### License

This software is proudly released under
[the GNU Affero General Public License v3.0 or later (AGPLv3) open-source license](LICENSE).

Its documentation is licensed under
[the Creative Commons Attributions-ShareAlike 4.0 International (CC BY-SA 4.0) license](docs/LICENSE).

Any contributions will be subject to the same licensing.

### Disclaimer

This project is intended as a means of unified access
to the digital flyer services of the various implemented providers.

It is designed with the interest of these companies in mind.
Strategies to reduce the load on their server infrastructure are one part of this effort.

The explicit goal of this project is not to reduce visits to their webpages
but to create a consistent and unified interface for all digital flyer services.
Easing and thus furthering the distribution of these products is the intended effect.

Use of the Cata-Log server and its codebase that is meant to harm individual companies,
while technically allowed under the license, is heavily discouraged.

This project is aimed at coexistence and cooperation with the companies,
benefiting both them and the open-source community.

[dockerhub]: https://hub.docker.com/r/dacid99/cata-log-hub
[pypi]: https://pypi.org/project/cata-log-hub
[readthedocs]: https://cata-log.readthedocs.io/latest/
