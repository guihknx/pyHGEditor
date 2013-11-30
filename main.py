#!/usr/bin/env python
## -*- coding: utf-8 -*-


import kivy
kivy.require('1.7.0')
from kivy.app import App
import codecs
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import sys; print sys.getdefaultencoding()
import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    text_input = ObjectProperty(None)
    savefile = ObjectProperty(None)


    def exit(self):
        self._popup.dismiss()

    def save_dialog(self):
        content = SaveDialog(save=self.save, cancel=self.exit)
        self._popup = Popup(title="Salvar...", content=content, )
        self._popup.open()


    def save(self, path, fname):
        with codecs.open(os.path.join(path, fname), 'w', 'utf8') as stream:
            stream.write(self.text_input.text)

        self.exit()


class myapp(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    myapp().run()

