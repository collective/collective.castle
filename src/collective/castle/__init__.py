# -*- coding: utf-8 -*-
"""Main product initializer
"""

from zope.i18nmessageid import MessageFactory
CastleMessageFactory = MessageFactory('collective.castle')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
