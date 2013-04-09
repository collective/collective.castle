collective.castle
=================

.. contents::

collective.castle is a Plone user interface for Products.CAS4PAS. 
CAS4PAS enables CAS-based authentication in Zope2 site containing PAS 
(the Pluggable Authentication System). All Plone 3.0 sites contain PAS.


Installation
============

This addon can be installed as any other Plone addons. Please follow the
official documentation_.

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to

Then, install CAS4PAS as a PAS plugin (see CAS4PAS documentation).

Check the controlpanel the /@@cas_control_panel configuration and voila, 
your site is now CAS-enabled!

You should remove the stock Plone login portlet so as not to confuse users.
You may, optionally, add the CAS Login portlet. Alternatively, you may simply
let users log in using the 'Log in' link at the upper-right of the Plone
window, as this is CAS-enabled.

plone.app.registry Configuration
================================

collective.castle uses plone.app.registry for maintaining values and as such,
GenericSetup can be used to import and export configuration. When values change
within settings in the registry, an event is fired such that the CAS4PAS plugin
and its settings are updated accordingly. For this reason, only modify 
settings on your CAS plugin. 

Example GenericSetup import configuration
-----------------------------------------

One GenericSetup import configuration profile looks like so within a
`profiles/default/registry.xml` (or similar) file::

    <registry>
      <record field="login_url" interface="collective.castle.interfaces.ICAS4PASPluginSchema" name="collective.castle.interfaces.ICAS4PASPluginSchema.login_url">
        <value>https://cas.secure.localhost/cas/login</value>
      </record>
      <record field="logout_url" interface="collective.castle.interfaces.ICAS4PASPluginSchema" name="collective.castle.interfaces.ICAS4PASPluginSchema.logout_url">
        <value>https://cas.secure.localhost/cas/logout</value>
      </record>
      <record field="session_var" interface="collective.castle.interfaces.ICAS4PASPluginSchema" name="collective.castle.interfaces.ICAS4PASPluginSchema.session_var">
        <value>__ac</value>
      </record>
      <record field="validate_url" interface="collective.castle.interfaces.ICAS4PASPluginSchema" name="collective.castle.interfaces.ICAS4PASPluginSchema.validate_url">
        <value>https://cas.secure.localhost/cas/validate</value>
      </record>
    </registry>

which can be placed into a policy product or similar for configuration. If 
doing so, ensure the given product's generic setup profile specifies 
collective.castle as a dependency in its `metadata.xml`::

    <?xml version="1.0"?>
    <metadata>
      <dependencies>
       <dependency>profile-collective.castle:default</dependency>
     </dependencies>
    </metadata>

Restricting user logins
-----------------------

By default, `collective.castle` allows any user that can authenticate to your
CAS server access to your portal. This may not always be suitable and 
an option is available to prevent authentication unless the user has a 
pre-determined role within your portal.

To enable this option, load the `CAS Configuration` control panel, and 
enable the `Users Require Role` option. This will now require any users
logging in via CAS to have some form of portal role associated with their
user account (aside from `Anonymous`) or else Plone will reject their 
authentication.

This implies that users accounts must be enumerable from some PAS plugin;
they could be created manually within Plone (`source_users`), provided from
another source such as LDAP or AD, or any other way you envisage.

Recreating CAS plugin
---------------------

If for some reason your CAS plugin is accidentally removed, or otherwise needs
repair, you can easily recreate it using the `Recreate Plugin` button on the
`CAS Configuration` control panel form.  This will remove an existing CAS
plugin (if present), and create a new one using the given settings.


Credits
=======

Companies
---------

- |QuadraInformatique|_

  * `Contact Quadra <mailto:plone@quadra-informatique.fr>`_


- |makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_


.. |QuadraInformatique| image:: http://www.quadra-informatique.fr/logo.png
.. _QuadraInformatique: http://www.quadra-informatique.fr/espace-clients/poles-dexpertises/xnet-zope-plone
.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

Authors
-------

- derek_richardson
- encolpe
- kiorky
- batlock666
- WouterVH
- davidjb
- etc.

Contributors
------------

- Thanks to the Georgia Institute of Technology for funding this product and allowing it to be released open-source. 
- Thanks to regebro and others who developed CAS4PAS.
- Finally, thanks to Alexandre Sauve, the author of the original PloneCASLogin who showed that this is possible.
