# Copyright (C) 2013 Fox Wilson, Peter Foley, Srijay Kasturi, Samuel Damashek, James Forcier and Reed Koser
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
from lxml.html import parse
from helpers.urlutils import get_short
from helpers.command import Command


@Command(['movie', 'imdb'])
def cmd(send, msg, args):
    """Gets a random movie.
    Syntax: !movie
    """

    html = parse(urlopen('http://www.imdb.com/random/title')).getroot()
    name = html.find('.//title').text.split('-')[0].strip()
    url = html.base_url.strip()
    send("%s -- %s" % (name, get_short(url)))
