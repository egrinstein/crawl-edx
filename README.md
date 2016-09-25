## MOOC Crawler -- Crawl EDx

Crawler using scrapy to get the data from EDx's courses.

Gets names, universities, review count and value, duration, weekly effort, etc.

when exporting to .csv using scrapy, some problem with the "&" character seems
to be messing up the line. Gonna build a pipeline to fix that when I have the time.

This crawl was made on September 24th, 2016. If EDx's site changes, the crawl
will probably stop working. If that happens, feel free to send me a message and
I might adapt it.


You can find a tutorial on how to crawl AJAX dependant pages at [this link](http://egrinstein.github.io/2016/10/25/scrapy-js/).
