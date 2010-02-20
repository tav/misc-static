"""
Quick Hack Script to Provide a Slightly Pretty Interface to the IRC Logs.

"""

import re

from DateTime import DateTime
from Products.PythonScripts.standard import html_quote

AMPIFY_TEMPLATE = u"""
<!DOCTYPE html>
<html>
<head>
	<title>Ampify :: %s</title>
	<meta http-equiv="content-language" content="en" />
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="author" content="Ampify Authors" />
	<meta name="description" content="These are the live chatlogs for the Ampify IRC channels." />
	<meta name="copyright" content="This work has been placed into the Public Domain." />
	<meta name="document-rating" content="general" />
	<link rel="stylesheet" type="text/css" media="screen" title="default" href="http://dev.ampify.it/css/site.css" />
    <style type="text/css">

      .right {
        text-align: right;
        border-right: 1px solid #4a525a;
        }

      a.grey, a.grey:active, a.grey:visited, a.grey:hover {
        color: #4a525a;
        text-decoration: none;
        }

      a.grey:hover {
        text-decoration: underline;
        }

      #irclogs {
	    border-collapse: collapse;
        width: 100%%;
	  }

      #irclogs td {
        padding: 4px;
        border-bottom: 1px dashed #4a525a;
      }

      #joinchat {
        font-size: 1.4em;
        text-align: center;
        margin: 10px 0 20px 0;
      }

    </style>
	<link rel="alternate" type="application/rss+xml" title="RSS Feed for Ampify" href="http://feeds.feedburner.com/ampify" />
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.min.js"></script>
	<script type="text/javascript" src="http://dev.ampify.it/js/site.js"></script>
</head>
<body>
<script type="text/javascript">
	var _gaq = [['_setAccount', 'UA-90176-28'], ['_trackPageview']];
	if (document.location.protocol !== 'file:') {
		(function() {
			var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
		})();
	}
</script>
<div id="body-outer"><div id="body-inner"><div id="body" class="clearfix">
<div id="header">
	<div id="menu-follow">
		<div><a href="http://www.facebook.com/Espians" title="Join Espians on Facebook"><img src="http://static.ampify.it/icon.facebook.gif" alt="Join Espians on Facebook" width="15px" height="15px" /></a></div>
		<div><a href="http://twitter.com/tav" title="Follow @tav on Twitter"><img src="http://static.ampify.it/icon.twitter.gif" alt="Follow @tav on Twitter" width="14px" height="14px" /></a></div>
		<div><a href="http://github.com/tav/ampify" title="Fork Ampify on GitHub"><img src="http://static.ampify.it/icon.github.png" alt="Join Espians on Facebook" width="15px" height="15px" /></a></div>
		<div><a href="http://feeds2.feedburner.com/ampify" title="Subscribe to the RSS Feed"><img src="http://static.ampify.it/icon.rss.png" alt="Subscribe to the RSS Feed" width="14px" height="14px" /></a></div>
	</div>
	<div id="logo"><a href="http://ampify.it"><img src="http://static1.ampify.it/logo.ampify.smallest.png" alt="Ampify" width="250px" height="56px" /></a></div>
	<div id="menu-lang">
		<a href="" title="Select Language" onclick="return reveal_language_options();"><img src="http://static.ampify.it/gfx.flag-uk.jpg" alt="Select Language" width="22px" height="15px" /></a>
		<br />
		<form id="menu-lang-form"><select id="menu-lang-select" onchange="google_translate_page(this);">
			<option value="" id="select_language">Select Language</option>
			<option value="&amp;langpair=en|af" id="openaf">Afrikaans</option><option value="&amp;langpair=en|sq" id="opensq">Albanian</option><option value="&amp;langpair=en|ar" id="openar">Arabic (&#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;)</option><option value="&amp;langpair=en|be" id="openbe">Belarusian</option><option value="&amp;langpair=en|bg" id="openbg">Bulgarian (&#1073;&#1098;&#1083;&#1075;&#1072;&#1088;&#1089;&#1082;&#1080;)</option><option value="&amp;langpair=en|ca" id="openca">Catalan (català)</option><option value="&amp;langpair=en|zh-CN" id="openzh-CN">Chinese (&#20013;&#25991; [&#31616;&#20307;])</option><option value="&amp;langpair=en|zh-TW" id="openzh-TW">Chinese (&#20013;&#25991; [&#32321;&#39636;])</option><option value="&amp;langpair=en|hr" id="openhr">Croatian (hrvatski)</option><option value="&amp;langpair=en|cs" id="opencs">Czech (&#269;esky)</option><option value="&amp;langpair=en|da" id="openda">Danish (Dansk)</option><option value="&amp;langpair=en|nl" id="opennl">Dutch (Nederlands)</option><option value="&amp;langpair=en|et" id="openet">Estonian</option><option value="&amp;langpair=en|fa" id="openfa">Farsi/Persian</option><option value="&amp;langpair=en|tl" id="opentl">Filipino</option><option value="&amp;langpair=en|fi" id="openfi">Finnish (suomi)</option><option value="&amp;langpair=en|fr" id="openfr">French (Français)</option><option value="&amp;langpair=en|gl" id="opengl">Galician</option><option value="&amp;langpair=en|de" id="opende">German (Deutsch)</option><option value="&amp;langpair=en|el" id="openel">Greek (&#917;&#955;&#955;&#951;&#957;&#953;&#954;&#940;)</option><option value="&amp;langpair=en|iw" id="openiw">Hebrew (&#1506;&#1489;&#1512;&#1497;&#1514;)</option><option value="&amp;langpair=en|hi" id="openhi">Hindi (&#2361;&#2367;&#2344;&#2381;&#2342;&#2368;)</option><option value="&amp;langpair=en|hu" id="openhu">Hungarian</option><option value="&amp;langpair=en|is" id="openis">Icelandic</option><option value="&amp;langpair=en|id" id="openid">Indonesian</option><option value="&amp;langpair=en|ga" id="openga">Irish</option><option value="&amp;langpair=en|it" id="openit">Italian (Italiano)</option><option value="&amp;langpair=en|ja" id="openja">Japanese (&#26085;&#26412;&#35486;)</option><option value="&amp;langpair=en|ko" id="openko">Korean (&#54620;&#44397;&#50612;)</option><option value="&amp;langpair=en|lv" id="openlv">Latvian (latviešu)</option><option value="&amp;langpair=en|lt" id="openlt">Lithuanian (Lietuvi&#371;)</option><option value="&amp;langpair=en|mk" id="openmk">Macedonian</option><option value="&amp;langpair=en|ms" id="openms">Malay</option><option value="&amp;langpair=en|mt" id="openmt">Maltese</option><option value="&amp;langpair=en|no" id="openno">Norwegian (norsk)</option><option value="&amp;langpair=en|pl" id="openpl">Polish (Polski)</option><option value="&amp;langpair=en|pt" id="openpt">Portuguese (Português)</option><option value="&amp;langpair=en|ro" id="openro">Romanian (Român&#259;)</option><option value="&amp;langpair=en|ru" id="openru">Russian (&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;)</option><option value="&amp;langpair=en|sr" id="opensr">Serbian (&#1089;&#1088;&#1087;&#1089;&#1082;&#1080;)</option><option value="&amp;langpair=en|sk" id="opensk">Slovak (sloven&#269;ina)</option><option value="&amp;langpair=en|sl" id="opensl">Slovenian (slovenš&#269;ina)</option><option value="&amp;langpair=en|es" id="openes">Spanish (Español)</option><option value="&amp;langpair=en|sw" id="opensw">Swahili</option><option value="&amp;langpair=en|sv" id="opensv">Swedish (Svenska)</option><option value="&amp;langpair=en|th" id="openth">Thai</option><option value="&amp;langpair=en|tr" id="opentr">Turkish</option><option value="&amp;langpair=en|uk" id="openuk">Ukrainian (&#1091;&#1082;&#1088;&#1072;&#1111;&#1085;&#1089;&#1100;&#1082;&#1072;)</option><option value="&amp;langpair=en|vi" id="openvi">Vietnamese (Ti&#7871;ng Vi&#7879;t)</option><option value="&amp;langpair=en|cy" id="opency">Welsh</option><option value="&amp;langpair=en|yi" id="openyi">Yiddish</option>		</select></form>
	</div>
	<div id="menu"><ul>
		<li><a href="http://blog.ampify.it">Blog</a></li>
		<li><a href="http://ampify.it/community.html" class="selected">Community</a></li>
		<li><a href="http://dev.ampify.it">Code</a></li>
		<li><a href="http://supporters.ampify.it">Supporters</a></li>
		<li><a href="http://ampify.it">About</a></li>
	</ul></div>
	<hr class="clear-left" />
	<div id="menu-sub"><a href="http://groups.google.com/group/ampify">Mailing List</a><span class="menu-sub-sep"> | </span><a href="http://help.ampify.it">Help Forums</a><span class="menu-sub-sep"> | </span><a href="http://irclogs.ampify.it">Chat Logs</a><span class="menu-sub-sep"> | </span><a href="http://webchat.freenode.net/?channels=esp">Live Chat</a></div>
	<hr class="clear" />
</div>

<div id="content">
%s
</div>

</div></div></div>
<div id="footer"><div id="footer-content">
<table id="footer-espians">
<tr id="footer-espians-tr"></tr>
</table>
<hr class="clear" />
<div class="footer-text">
  <div class="footer-menu">
    <a href="http://ampify.it">ABOUT</a>
    &middot; <a href="http://supporters.ampify.it">SUPPORTERS</a>
    &middot; <a href="http://dev.ampify.it">CODE</a>
    &middot; <a href="http://ampify.it/community.html">COMMUNITY</a>
    &middot; <a href="http://blog.ampify.it">BLOG</a>
  </div>
  <div>
	<a href="http://ampify.it/#help-spread-the-word" title="Help Spread The Word"><img src="http://static.ampify.it/gfx.help-spread-the-word.png" id="spread-button" alt="Help Spread The Word" width="372px" height="30px" /></a>
  </div>
</div>
<hr class="clear" />
</div></div>
</body>
</html>
""".encode('utf-8')

DEFAULT_TEMPLATE = """

<html>
  <head><title>%s</title></head>
  <body>
    %s
  </body>
</html>

"""

# ------------------------------------------------------------------------------
# some constants
# ------------------------------------------------------------------------------

request = container.REQUEST
response =  request.RESPONSE

response.setHeader('content-type', 'text/html; charset=utf-8')

log_directory = '/home/jja/var/supybot/logs/ChannelLogger/'
prefix_len = len(log_directory)
ts = traverse_subpath

if request.HTTP_HOST == 'irclogs.ampify.it':
  active_channels = ['esp']
  if as_index:
    ts = ['esp', 'latest']
  template = AMPIFY_TEMPLATE
else:
  active_channels = ['24weeks','beerusergroup','esp','esp-core','green','logilogi','opencoop','tribalradix','ud','openkollab','okcore']
  template = DEFAULT_TEMPLATE

month_names = [

    None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'

    ]

month_names_full = [

    None, 'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'

    ]


now = DateTime()
today = now.year(), now.month(), now.day()

# ------------------------------------------------------------------------------
# some regexps
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# utility functions
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# display a channel list
# ------------------------------------------------------------------------------

if not ts or ts[0] not in active_channels:

    channel_list = []

    for channel in active_channels:
        channel_list.append('<li><a href="%s/%s" title="#%s IRC Channel Logs">#%s</a></li>' % (script.absolute_url(), channel, channel, channel))

    return template % ('IRC Logs', """
    <h3>IRC Logs</h3>
    <ul>
      %s
    </ul>

""" % ''.join(channel_list))

# ------------------------------------------------------------------------------
# display a prettified irc log
# ------------------------------------------------------------------------------

channel = ts.pop(0)

if channel == 'esp-core':
  if 'Espian' not in _.SecurityGetUser().getRoles():
    raise 'Unauthorized'

if channel == 'okcore':
  if 'OKCore' not in _.SecurityGetUser().getRoles():
    raise 'Unauthorized'

if ts:

    # examples of possible options
    # /tail will show the last 20 lines of today's log
    # /XxXxX/<number> will show the last <number> of today's log
    # /<year>/<month>/<day> will show that date's log
    # /<year>/<month>/<day>/<startline>/<endnumber> will show from <startline> to <endline>

    limit = 0
    slice = 0

    if ts and ts[-1] == 'full':
      ts.pop()
      chatonly = 0
    else:
      chatonly = 1

    if len(ts) == 1:
        year, month, day = today
        if ts[0] == 'tail':
          limit = 20
    elif len(ts) == 2:  #why? shouldn't this be simpler?
        year, month, day = today
        limit = int(ts[1])
    elif len(ts) == 3:
        year, month, day = map(int, ts)
    elif len(ts) == 5:
        year, month, day = map(int, ts[:3])
        slice = int(ts[3])
        limit = int(ts[4])
    else:
        year, month, day = today

    try:
      log = [
          line[13:] for line in context.render_log(
            logdate=("%02d%s%d" % (
              day, month_names[month], year)
            ),
            channel=channel).splitlines()
          ]
    except IOError:
      log = []

    if slice and limit:
        log = log[slice:limit+1]
    elif limit:
        log = log[-limit:]

    def replace_html_link(content):
        ref = content.group(1)
        if ref.endswith('&gt;'):
            ref = ref[:-4]
            return r'<a href="%s">%s</a>&gt;' % (ref, ref[:100])
        return r'<a href="%s">%s</a>' % (ref, ref[:100]) # for really long urls
        #return r'<a href="\1">\1</a>'

    newlog = []

    for index, line in enumerate(log):

        line = html_quote(line)

        # make html links

        line = re.sub(
            r'((plex|mailto|http|https|ftp|irc|gopher|news)://[^ \'")<>]*)',
            replace_html_link, line)

        # convert some control characters to html elements

        line = re.sub('\x02([^\x02]*)\x02', r'<strong>\1</strong>', line)
        line = re.sub('\x1f([^\x1f]*)\x1f', r'<em>\1 </em>', line)

        # strip out other control characters

        line = ''.join([char for char in line if ord(char) > 31])

        timestamp, message = line.split(']', 1)

        timestamp_id = timestamp.replace(':', '-')

        timestamp = '<a href="#%s" id="%s" class="grey">%s</a>' % (
            timestamp_id, timestamp_id, timestamp
            )

        message = message.strip()

        if message.startswith('*** '):

            if chatonly:
                continue

            split_message = message.split()
            message_type = split_message[3:4] and split_message[3] or ''

            if message_type == 'joined':
                nickname = '&rarr;'
                message = "%s joined" % split_message[1]
            elif message_type == 'quit':
                nickname = '&larr;'
                message = "%s left" % split_message[1]
            else:
                nickname = '***'
                message = message[4:]

        elif message.startswith('* '):
            nickname = '*'
            message = message[2:]

        else:
            message = message.split('&gt; ', 1)
            if len(message) == 2:
                nickname, message = message
            else:
                message, nickname = message[0], ""
            nickname = '<span class="grey">&lt;</span>%s' \
                       '<span class="grey">&gt;</span>' % nickname[4:]

        line = (
         '<tr><td class="right" valign="top">%s </td><td>%s</td><td valign="top"> %s</td></tr>'
         % (nickname, message, timestamp)
         )

        newlog.append(line)

    # print it!

    # log = '\n<br />'.join(log)
    log = '\n'.join(newlog)

    # full / previous / next
    log_date = DateTime('%s/%02d/%02d' % (year, month, day))
    prev_date = log_date - 1

    if limit:
        prevnext = '<a href="%s">&larr; entire log</a>' % log_date

    if not limit:
        prevnext = '<a href="%s/%s/%s%s">&larr; previous day</a>' % (
            script.absolute_url(), channel, prev_date.strftime('%Y/%m/%d'),
            (not chatonly) and "/full" or ""
            )

    if chatonly:
        prevnext += ' | <a href="%s/%s/%s/full">full log</a>' % (
          script.absolute_url(), channel, log_date
          )
    else:
        prevnext += ' | <a href="%s/%s/%s">chat only</a>' % (
          script.absolute_url(), channel, log_date
          )

    if (year, month, day) != today:
        prevnext += ' | <a href="%s/%s/%s%s">next day &rarr;</a>' % (
            script.absolute_url(), channel, (log_date + 1).strftime('%Y/%m/%d'),
            (not chatonly) and "/full" or ""
        )

    if newlog:
        endlink = prevnext
    else:
        endlink = ""

    if template == DEFAULT_TEMPLATE:

        print """

<html>
  <head>
    <title>IRC Log for #%s on %s/%02d/%02d</title>
    <style type="text/css">

      body {

        font-family: Georgia;

        }

      .right {
        text-align: right;
        border-right: 1px solid #4a525a;
        }

      .grey {
        color: #4a525a;
        text-decoration: none;
        }

      table {
	    border-collapse: collapse;
        width: 100%%;
	  }

      td {
        border-bottom: 1px dashed #4a525a;
      }

    </style>
  </head>
  <body>
    <h3><a href="%s/%s">IRC Log for #%s</a> on %s/%02d/%02d</h3>

    <br /><br />

    Find this useful?  Consider donating! <br>
    <!-- Begin PayPal Logo -->
    <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="image" src="https://www.paypal.com/en_US/i/btn/x-click-but21.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----">
    </form>
    <!-- End PayPal Logo -->

    %s<br /><br />

    <table cellspacing="0" cellpadding="4">
    %s
    </table>

    <br />
    %s

  </body>
</html>

""" % (channel, year, month, day, script.absolute_url(), channel, channel, year,
       month, day, prevnext, log, endlink)

        return printed

    else:

        return template % (
            "IRC Log for #%s on %s/%02d/%02d" % (channel, year, month, day),
            """
    <h3><a href="%s/%s">IRC Log for #%s</a> on %s/%02d/%02d</h3>
    <div id="joinchat">
    Join the chat on <code>irc.freenode.net/%s</code> right now using
    <a href="http://webchat.freenode.net/?channels=%s">webchat</a>.
    </div>
    %s<br /><br />

    <table cellspacing="0" cellpadding="4" id="irclogs">
    %s
    </table>

    <br />
    %s
            """ % (script.absolute_url(), channel, channel, year, month, day, channel, channel, prevnext, log, endlink)
            )

# ------------------------------------------------------------------------------
# display a list of available logs
# ------------------------------------------------------------------------------

else:

  hash_channel = '#' + channel + '.'
  len_channel = len(hash_channel)

  index = context.render_index(channel)
  index = [(file[len_channel+5:len_channel+9], month_names.index(file[len_channel+2:len_channel+5]), file[len_channel:len_channel+2]) for file in [file[prefix_len:-4] for file in index] if file.startswith(hash_channel)]

  logs_list = []
  append_to_logs_list = logs_list.append

  index.sort()

  for year, month, day in index[::-1]:
    append_to_logs_list('<li><a href="%s/%s/%s/%02d/%02d">%s %s %s</a></li>' % (script.absolute_url(), channel, year, int(month), int(day), day, month_names_full[month], year))

  return template % ("IRC Logs for #%s" % channel, """
    <h3>IRC Logs for #%s</h3>
    <ul>
      %s
    </ul>
"""% (channel, ''.join(logs_list)))

  return printed
