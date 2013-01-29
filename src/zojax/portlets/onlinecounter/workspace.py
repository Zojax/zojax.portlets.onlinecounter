##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface, component, event
from zojax.content.space.interfaces import IRootSpace
from zojax.content.space.workspace import WorkspaceFactory
from zojax.content.type.container import ContentContainer

from interfaces import _, IVisitorsViewWorkspace, IVisitorsViewWorkspaceFactory


class VisitorsViewWorkspace(ContentContainer):
    interface.implements(IVisitorsViewWorkspace)

    @property
    def space(self):
        return self.__parent__


class VisitorsViewWorkspaceFactory(WorkspaceFactory):
    component.adapts(IRootSpace)
    interface.implements(IVisitorsViewWorkspaceFactory)

    name = 'visitors_view'
    title = _(u'Statistic of visitors')
    description = _(u'Workspace with list of visitors.')
    weight = 222
    factory = VisitorsViewWorkspace
