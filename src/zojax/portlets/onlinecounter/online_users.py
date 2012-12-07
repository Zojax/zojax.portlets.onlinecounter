import datetime
from zojax.resourcepackage.library import includeInplaceSource
from zope.app.security.interfaces import IUnauthenticatedPrincipal

from zojax.content.type.item import PersistentItem
from zojax.content.type.container import ContentContainer
from zojax.portlets.onlinecounter.interfaces import IStatCounters
from zope import interface
from zope.schema.fieldproperty import FieldProperty
from zope.component import getUtility, queryMultiAdapter
from zope.app.intid.interfaces import IIntIds
from zope.app.component.hooks import getSite


class OnlineUsersPortlet(object):

    def isAvailable(self):
        return not IUnauthenticatedPrincipal.providedBy(self.request.principal) 
    
    def render(self):
        includeInplaceSource("<script type='text/javascript'>$(document).ready(makeOnline());$('#online_number').ready(getOnlineNumber('online_number'));</script>")
        return super(OnlineUsersPortlet, self).render()

    def format_date(self, date):
        new_date = str(date.day) + '.' + str(date.month) + '.' + str(date.year) + ' ' + str(date.hour)+ ':'
        if len(str(date.minute))==1:
            new_date += '0' + str(date.minute)
        else:
            new_date += str(date.minute)
        return new_date

    def update(self):
        site = getSite()
        max_online = "Max online - "
        max_logged = "Max logged - "
        try:
            max_count = sorted(site['stats'].count_users_by_month, key=lambda x: x[0], reverse=True)[0]
            self.stats_max_online = max_online + str(max_count[0]) + ' (' + self.format_date(max_count[1]) +')'
            stats_max_logged = sorted(site['stats'].count_users_names, key=lambda x: x[0], reverse=True)[0]
            self.stats_max_logged = max_logged + str(stats_max_logged[0]) + ' (' + self.format_date(stats_max_logged[1]) +')'
        except (IndexError,KeyError), e:
            try:
                max_count = sorted(site['stats'].count_users_allday, key=lambda x: x[0], reverse=True)[0]
                self.stats_max_online = max_online + str(max_count[0]) + ' (' + self.format_date(max_count[1]) +')'
                stats_max_logged = len(site['stats'].list_users_names)
                self.stats_max_logged = max_logged + str(stats_max_logged) + ' (' + self.format_date(datetime.datetime.now()) +')'
            except (IndexError,KeyError, AttributeError), e:
                self.stats_max_online = max_online + ' None'
                self.stats_max_logged = max_logged + ' None'

class StatCounters(PersistentItem):
    interface.implements(IStatCounters)
    count_users_online_now = FieldProperty(IStatCounters['count_users_online_now'])
    count_users_allday = FieldProperty(IStatCounters['count_users_allday'])
    count_users_by_month = FieldProperty(IStatCounters['count_users_by_month'])
    list_users_names = FieldProperty(IStatCounters['list_users_names'])
    count_users_names = FieldProperty(IStatCounters['count_users_names'])

    @property
    def id(self):
        return getUtility(IIntIds).getId(self)
