#!/usr/bin/env python
import kivy
kivy.require('1.7.0')
from kivy.core.window import Window
from kivy.app import App
import codecs
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.uix.scrollview import ScrollView
from  kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.config import Config
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
    label_wid = ObjectProperty()
    label_modified = ObjectProperty()
    info = StringProperty()


    def set_file(self, text):
        self.label_wid.text = text

    def set_modified(self, text):
        self.label_modified.text = text

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
        with codecs.open(os.path.join(path, filename[0]  or ''), 'r','utf-8') as stream:
            self.text_input.text = stream.read()
        print(filename)
        self.set_file(filename[0].encode("ascii"))
        self.set_modified('Modified: NO')
        self.exit()

    def save(self, path, fname):
        with codecs.open(os.path.join(path, fname or ''), 'w', 'utf8') as stream:
            stream.write(self.text_input.text)
        self.set_file(fname)
        self.set_modified('Modified: NO')
        self.exit()


class myapp(App):
    def build(self):
        self.title = 'pyHGEditor'
        pass


Factory.register('Root', cls=Root)
Factory.register('OpenDialog', cls=OpenDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    myapp().run()

