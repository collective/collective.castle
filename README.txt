collective.castle
-----------------

collective.castle is a Plone 3.0 (and up) user interface for Products.CAS4PAS. 
CAS4PAS enables CAS-based authentication in Zope2 site containing PAS 
(the Pluggable Authentication System). All Plone 3.0 sites contain PAS.

Installation
------------
To install, simply include the egg in your buildout (don't forget to hook up
the zcml). Then, install CAS4PAS as a plugin as usual (see CAS4PAS 
documentation). Finally, install collective.castle from the Plone control
panel. Your site is now CAS-enabled!

You should remove the stock Plone login portlet so as not to confuse users.
You may, optionally, add the CAS Login portlet. Alternatively, you may simply
let users log in using the 'Log in' link at the upper-right of the Plone
window, as this is CAS-enabled.

Versions
--------
1.0 - Released May 2, 2008
    - Initial release
      [derek_richardson]
      
Credits
-------
Thanks to the Georgia Institute of Technology for funding this product and
allowing it to be released open-source. Thanks to regebro and others who
developed CAS4PAS. Finally, thanks to Alexandre Sauve, the author of the 
original PloneCASLogin who showed that this is possible.