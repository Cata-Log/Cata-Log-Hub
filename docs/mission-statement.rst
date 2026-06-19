..
   SPDX-License-Identifier: CC-BY-SA 4.0

   Copyright (C) 2026 David Aderbauer & The Cata-Log Contributors
   Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Mission Statement
=================

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
