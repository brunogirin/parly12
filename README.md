Rewired State Parliament 2012 Hack
==================================

The Brief
---------

This is a simple [django](https://www.djangoproject.com/) application
created for [Rewired State Parliament 2012](http://rewiredstate.org/hacks/parliament-2012)
that generates graphs from voting behavour by British Members of Parliament
held in a database. I worked with
[Charlie Perrins](http://twitter.com/charlieperrins) who came up with the
original idea and collated all source data; and
[Ela Osterberger](http://twitter.com/CuteNumbers) who did some brilliant
analytics work. Full details and a presentation of the hack
[are available on the Rewired State hack page](http://hacks.rewiredstate.org/events/parlyhack-2012/mps-legislative-rainy-day-fun-pack).

Usage
-----

In order to run the application, unpack everything, install django then
navigate to the `parly2012` directory in a terminal and run the following:

    ./manage.py collectstatic
    ./manage.py syncdb
    ./manage.py runserver

This will start a lightweight web server that you will be able to access at
the following URL: <http://localhost:8000>

You will first be presented with a page that asks you to load the data set.
Note that loading the full data set takes quite a long time.

Take Away
---------

As ever with with hack days, there was the opportunity to learn new things,
some of those are implemented in the code:
* How to [execute custom SQL in django](https://docs.djangoproject.com/en/dev/topics/db/sql/#executing-custom-sql-directly);
* How to [create inline SVG in HTML5](http://www.w3schools.com/html/html5_svg.asp)
and generate it in a django template.

The hack does interesting stuff but is limited by the fact that the data is
held in a SQL database. More interesting graphs could probably be generated by
using a no-SQL database such as [riak](http://wiki.basho.com/) or by using
a statistical language such as [R](http://www.r-project.org/), which were
investigated but discarded as too complicated due to time constraints:
* How to [embed R code in python](http://rpy.sourceforge.net/);
* How to [call Riak from django](https://github.com/basho/riak-python-client).

---------------------------------------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

