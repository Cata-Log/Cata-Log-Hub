Usage
=====

Nomenclature
------------

Before we get into details on how Cata-Log works, we have to get the wording straight.

- Catalog: Collective term for any type of digital print product meant to advertise store offers and price reductions. This includes flyers, weekly ads, etc.
- Store: Publisher of at least one catalog. Typically large store chains that offer digital catalogs.
- Provider: Source of a single catalog. There can be more than one provider per store.
    For instance, a store may offer one catalog for current offers and a catalog for offers in the next week.
    Each of these catalogs is considered to have their own provider.
    Providers for catalogs that concern the future are often distinguished by the suffix -preview.

Concept
-------

The Cata-Log server consists of three main components:

- A task backend that runs routine tasks to cache the digital catalog for every configured provider.
- A database (sqlite3 by default) in which the cached catalogs and their pages are indexed.
- A web frontend to interact with that data.

In practice the first two are only of concern for the server admin.

Frontend
--------

Users interact with the frontend which can be further divided into four subsections.

Webinterface
^^^^^^^^^^^^

This webinterface, located at the URL root is meant for simple and user-friendly management of providers and their configuration.
It does not offer all capablities of the API.

API
^^^

All data is available through the API endpoints.
Its complete documentation can be found at */docs/swagger* and */docs/redoc* .

Static Files
^^^^^^^^^^^^

Cata-Log serves all catalog page images as static files under */static/pages* . The name of the individual files can be retrieved via the API.
This complements the download and embed options for maximum flexiblity for third-party developers.

Additionally, some components of the webui are also static but are served under a different path.

OPDS
^^^^

To allow reading the cached catalogs with an e-reader device, a complete OPDS catalog is offered under */opds* .
Use it to browse providers and their catalogs.
These endpoints only read data.

Setting up your providers
-------------------------

The process of configuring the providers you need it straightforward.
Every provider is preconfigured as much as possible, including its caching schedule and frequency.

The only configuration that is still required are the ones that can't decided for you during development.
In most cases these configurations define your local branch or region of the store and provider.

You can decide between using the API or API schema docs to create individual providers or the webinterface which offers a more user-friendly experience.

After a provider is created, its catalog will be cached right away. That may take a few moments.

Accessing the cached catalogs
-----------------------------

The data for every catalog can be accessed in various ways.

Catalog
^^^^^^^

If you wish to get the catalog as a whole, you can retrieve it

- as pdf download from API (*/api/v1/catalogs/{catalog_id)/download*)
- as pdf embedding from API (*/api/v1/catalogs/{catalog_id)/embed*)
- as epub from OPDS (*/opds/{catalog_id}.epub*)

Pages
^^^^^

Every single page of a catalog is made available in three different ways

- API download (*/api/v1/catalogs/{catalog_id}/download*)
- API embedding (*/api/v1/catalogs/{catalog_id}/embed*)
- static file (*/static/pages/{page_filename}*)

All pages are stored in webp format for modern compression and generally smaller sizes.
