import sys

import pygame
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from config_midi import ConfigMidi
from midi_generator import MidiGenerator
from midi_player import MidiPlayer
from song import Song


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        pygame.init()
        self.thread = None
        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.thread is not None and self.thread.isRunning():
            self.thread.terminate()
            self.thread.wait()
            self.thread = None
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
        if self.thread is not None:
            self.thread.terminate()
        self.thread = QtCore.QThread()
        self.thread.run = self.write_music
        self.thread.start()
        """ 
        self.write_music()
        """

    def getColor(self, x, y):
        pixel = self.pixmap().toImage().pixel(x, y)
        color = QtGui.QColor.fromRgba(pixel)
        return color

    def write_music(self):
        drumscore = ""
        for i in range(0, self.width(), 10):
            for j in range(0, self.height(), 20):
                color = self.getColor(i, j)
                if color.red() < 1 / 2:
                    print(i, j, color)
                    drumscore += str(int(j / self.height() * 68)) + "|"
                    print()
        song1 = Song(True, drumscore=drumscore)

        MIDI_FILENAME = "test_midi.mid"

        config_midi = ConfigMidi(song1.ensemble, 200, 30)
        midi_generator = MidiGenerator(config_midi)
        midi_generator.read_score("|", 1)
        midi_generator.write_file(MIDI_FILENAME)
        self.play(MIDI_FILENAME)

        """
        self.thread.terminate()
        self.thread.wait()
        """

    def play(self, midi_file=""):

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(midi_file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                print("Music stopped playing.")
                break
