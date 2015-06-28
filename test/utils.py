from django.conf.urls import url
from dashing.views import Dashboard


class Router(object):
    def __init__(self):
        self.registry = []

    def register(self, widget, basename, *args, **kwargs):
        """ Register a widget, URL basename and any optional URL parameters.

        Parameters are passed as keyword arguments, i.e.
            >>> router.register(MyWidget, 'mywidget', my_parameter="[A-Za-z0-9_-]+")

        This would be the equivalent of manually adding the following
        to urlpatterns:
            >>> url(r"^widgets/mywidget/(P<my_parameter>[A-Z0-9]+)/?",
                                         MyWidget.as_view(), "widget_mywidget")

        """
        self.registry.append((widget, basename, args, kwargs))

    def get_urls(self):

        urlpatterns = [
            url(r'^$', Dashboard.as_view(), name='dashboard'),
        ]

        for widget, basename, args, parameters in self.registry:
            urlpatterns += [
                url(r'/'.join((
                    r'^widgets/{}'.format(basename),
                    r'/'.join((r'(?P<{}>{})'.format(param, parameters[param])
                               for param in args)),
                )),
                    widget.as_view(),
                    name='widget_{}'.format(basename)),
            ]

        print "---urlpatterns---"
        print urlpatterns
        print "--------------"
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()


router = Router()
