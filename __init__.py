#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import, print_function)

__license__   = 'GPL v3'
__copyright__ = '2012, Fresco Gamba <robot@yugo.at>'
__docformat__ = 'restructuredtext en'

# The class that all Interface Action plugin wrappers must inherit from
from calibre.customize import InterfaceActionBase

class WordpressPlugin(InterfaceActionBase):
    name                = 'Wordpress Plugin'
    description         = 'A plugin to automatically create wordpress posts out of calibre'
    supported_platforms = ['windows', 'osx', 'linux']
    author              = 'Fresco Gamba'
    version             = (1, 0, 0)
    minimum_calibre_version = (0, 7, 53)
    actual_plugin       = 'calibre_plugins.wordpress_plugin.ui:WordpressPluginUI'

    def is_customizable(self):
        return True

    def config_widget(self):
        # It is important to put this import statement here rather than at the
        # top of the module as importing the config class will also cause the
        # GUI libraries to be loaded, which we do not want when using calibre
        # from the command line
        from calibre_plugins.wordpress_plugin.config import ConfigWidget
        return ConfigWidget()

    def save_settings(self, config_widget):
        config_widget.save_settings()

        # Apply the changes
        ac = self.actual_plugin_
        if ac is not None:
            ac.apply_settings()


