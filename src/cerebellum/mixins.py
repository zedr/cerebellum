# noinspection PyUnresolvedReferences
class WidgetHelper(object):
    """A mixin that adds helper methods to any widget.
    """

    def get_widget_by_name(self, name):
        for widget in self.walk():
            if hasattr(widget, "name"):
                if widget.name == name:
                    return widget
