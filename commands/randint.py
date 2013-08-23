# Copyright (C) 2013 Fox Wilson, Peter Foley, Srijay Kasturi, Samuel Damashek and James Forcier
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from urllib.request import urlopen


def gen_random(msg):
    #msg = quote(msg)
    if msg.isdigit() and int(msg) < 1000000000:
        msg = int(msg)
    else:
        msg = 1000000000
    html = urlopen('http://www.random.org/integers/?num=1&min=1&max=%d&col=1&base=10&format=plain&rnd=new' % msg,
                   timeout=2).read().decode()
    return html


def cmd(send, msg, args):
    """Gets a random integer.
    Syntax: !random <maximum length>
    """
    random = gen_random(msg)
    send(random)