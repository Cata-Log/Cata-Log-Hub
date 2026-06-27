# Cata-Log Hub

The central hub for digital flyers.

If you can check at least two of the following, this project is for you:

- [ ] You like to shop items that are on offer.
- [ ] You like to check what's on offer before you go to the store.
- [ ] You care about privacy.
- [ ] You want to use open-source software.

## Mission

There exist proprietary shopping list apps (which shall not be named here)
that have a viewer for the current offers at various grocery store chains.

This is a feature that has so far not been available
in open-source shopping-list applications.

One main roadblock is the fact that all stores use different implementations
of their online flyers, creating a massive implementation and maintenance
workload for the developers of such apps, should they consider such a feature.

It is the mission of the Cata-Log project to change this status quo.

Cata-Log's main component is a server with interfaces for a multitude of
digital flyer implementations.
It regularly retrieves and caches the online flyers
from user-selected providers.
This data is then offered to third-party applications via
a consistent, unified and comprehensive API.

This way, the load of implementing and maintaining the various interfaces
to the online flyers is distributed onto the shoulders
of the Cata-Log contributors, instead of a single developer.

To further the ease of adaption for third-party developers,
the Cata-Log project includes client-libraries to its API for various languages,
including Java and Swift for mobile- as well as Javascript for web-development.

Adding new flyer providers to Cata-Log is designed to be as easy as possible.
A provider interface is defined by a single Python3 class.
The documentation gives an extensive example and guideline for its implementation.

It's the ultimate goal of the Cata-Log project to have a viewer for
current store offers in the major open-source shopping-planning applications.

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

## Installation

The Cata-Log-Hub server is intended to be run
either with the container image provided at [dockerhub][dockerhub]
or bare-metal with the [python-package][pypi].

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

Install the cata-log python package. It requires at least python3.14.

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

## Documentation

The full documentation is available on [ReadTheDocs][readthedocs].

## Contributing

THIS PROJECT LIVES FROM YOUR CONTRIBUTIONS!

If there is a provider class you are missing, give implementing it a try.
The quickstart and guide for implementing a provider class are in the documentation.

Thank you to [everybody who helped with advancing this project](CONTRIBUTORS.md)
and [who helped with translation](TRANSLATORS.rst)!

## Legal

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
