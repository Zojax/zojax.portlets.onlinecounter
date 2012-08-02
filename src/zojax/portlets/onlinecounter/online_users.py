from zojax.resourcepackage.library import includeInplaceSource
from zope.app.security.interfaces import IUnauthenticatedPrincipal

class OnlineUsersPortlet(object):

    def isAvailable(self):
        return not IUnauthenticatedPrincipal.providedBy(self.request.principal) 
    
    def render(self):
        includeInplaceSource("<script type='text/javascript'>$(document).ready(makeOnline());$('#online_number').ready(getOnlineNumber('online_number'));</script>")
        return super(OnlineUsersPortlet, self).render()