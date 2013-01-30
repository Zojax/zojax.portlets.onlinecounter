import zope.schema

from zojax.widget.list.field import SimpleList
from zojax.content.space.interfaces import IContentSpace, IRootSpace, IWorkspace, IWorkspaceFactory
from zojax.content.space.workspace import WorkspaceFactory
from zojax.content.type.interfaces import IItem

from zope import interface
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('zojax.quick.contenttypes')

class IOnlineUsersPortlet(interface.Interface):
    """ Online users portlet """


class IStatCounters(interface.Interface):
    count_users_online_now = zope.schema.Int(title=u"count_users_online_now",required=False)
    count_users_allday = SimpleList(title = _(u'count_users_allday'),required = False)
    count_users_by_month = SimpleList(title = _(u'count_users_by_month'),required = False)
    list_users_names = SimpleList(title = _(u'list_users_names'),required = False)
    count_users_names = SimpleList(title = _(u'count_users_names'),required = False)


class IVisitCount(interface.Interface):
    """ Interface for classes, that must store visit statistic of object """
    visitors_number = zope.schema.Int(title=u"number of visits",required=False)
    visitors_list = SimpleList(title = _(u'visitors'),required = False)

    def drop_counter(self):
        pass

    def inc_counter(self):
        pass

    def add_user(self, user):
        pass

    def get_users(self):
        pass


class IVisitCountable(interface.Interface):
    """ Allows classes to be adapted for getting visit-counter feature """
