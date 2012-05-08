collective.castle
=================

.. contents::

collective.castle is a Plone 3.0 (and up) user interface for Products.CAS4PAS. 
CAS4PAS enables CAS-based authentication in Zope2 site containing PAS 
(the Pluggable Authentication System). All Plone 3.0 sites contain PAS.


Installation
============
To install, see docs/INSTALL.txt.
Then, install CAS4PAS as a plugin as usual (see CAS4PAS
documentation). Finally, install collective.castle from the Plone control
panel. Your site is now CAS-enabled!

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
