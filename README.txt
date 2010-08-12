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
- etc.

Contributors
------------

- Thanks to the Georgia Institute of Technology for funding this product and allowing it to be released open-source. 
- Thanks to regebro and others who developed CAS4PAS.
- Finally, thanks to Alexandre Sauve, the author of the original PloneCASLogin who showed that this is possible.
