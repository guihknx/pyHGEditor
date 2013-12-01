#!/usr/bin/env python
## -*- coding: utf-8 -*-


import kivy
kivy.require('1.7.0')
from kivy.app import App
import codecs
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.uix.scrollview import ScrollView
from  kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import sys; print sys.getdefaultencoding()
import os

class MainWidget(FloatLayout):
    manager = ObjectProperty(None)

class OpenDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    text_input = ObjectProperty(None)
    savefile = ObjectProperty(None)
    loadfile = ObjectProperty(None)
    root = ScrollView(size_hint=(None, None), size=(400, 400),
    pos_hint={'center_x':.5, 'center_y':.5})

    def exit(self):
        self._popup.dismiss()

    def save_dialog(self):
        content = SaveDialog(save=self.save, cancel=self.exit)
        self._popup = Popup(title="Salvar...", content=content, )
        self._popup.open()

    def open_dialog(self):
        content = OpenDialog(load=self.load, cancel=self.exit)
        self._popup = Popup(title="Selecione o arquivo", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with codecs.open(os.path.join(path, filename[0]), 'r','utf-8') as stream:
            self.text_input.text = stream.read()
        self.exit()

    def save(self, path, fname):
        with codecs.open(os.path.join(path, fname), 'w', 'utf8') as stream:
            stream.write(self.text_input.text)
        self.exit()


class myapp(App):
    pass



Factory.register('Root', cls=Root)
Factory.register('OpenDialog', cls=OpenDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    myapp().run()

