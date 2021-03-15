#
#  Sharktest
#  Programs for testing Megalodon.
#  Copyright the Megalodon authors 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import os
import random
import socket
import chess
import chess.engine

PARENT = os.path.dirname(os.path.realpath(__file__))
ENG_PATH = os.path.join(PARENT, "Megalodon")

PARAMS = (
    "EvalCenter",
)
BATCH_SIZE = 50


def rand_configure(engine, weights):
    for i in range(len(PARAMS)):
        engine.configure({PARAMS[i]: weights[i]})
    return engine


def play_games():
    results = []
    weights = [random.randint(0, 1000) for i in PARAMS]
    for i in range(BATCH_SIZE):
        white = chess.engine.SimpleEngine.popen_uci(ENG_PATH)
        black = chess.engine.SimpleEngine.popen_uci(ENG_PATH)
        if random.random() < 0.5:
            white = rand_configure(white, weights)
        else:
            black = rand_configure(black, weights)


def main():
    while True:
        results = play_games()


main()
