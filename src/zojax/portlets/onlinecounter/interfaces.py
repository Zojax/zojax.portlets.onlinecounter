from zope import interface
import zope.schema
from zojax.widget.list.field import SimpleList
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('zojax.quick.contenttypes')
#from zojax.authentication.portlets.interfaces import _

class IOnlineUsersPortlet(interface.Interface):
    """ Online users portlet """


class IStatCounters(interface.Interface):
    count_users_online_now = zope.schema.Int(title=u"count_users_online_now",required=False)
    count_users_allday = SimpleList(title = _(u'count_users_allday'),required = False)
    count_users_by_month = SimpleList(title = _(u'count_users_by_month'),required = False)
    list_users_names = SimpleList(title = _(u'list_users_names'),required = False)
    count_users_names = SimpleList(title = _(u'count_users_names'),required = False)