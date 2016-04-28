"""
Usage: new_category <tag|category> <slug> <name>
"""

import sys, os.path

tag_or_category = sys.argv[1] if len(sys.argv) > 1 else '';
slug = sys.argv[2] if len(sys.argv) > 2 else '';
name = sys.argv[3] if len(sys.argv) > 3 else '';

if tag_or_category == '':
  print __doc__
  sys.exit(0)
if not (tag_or_category == 'tag' or tag_or_category == 'category'):
  print __doc__
  sys.exit(0)
if slug == '' or name == '':
  print __doc__
  sys.exit(0)

# create tag/category dir, then create tag/category page
try:
  os.makedirs(tag_or_category)
except OSError:
  if not os.path.isdir(tag_or_category):
    raise
category_page = open(tag_or_category +'/' + slug + '.md', 'w')
category_page.write('---\n')
category_page.write('layout: blog_by_' + tag_or_category + '\n')
category_page.write(tag_or_category + ': ' + slug + '\n')
category_page.write('permalink: ' + tag_or_category + '/' + slug + '/\n')
category_page.write('---\n')

# create _data/<categories|tags> if it doesn't exist, then append the
# category/tag to the list
try:
  os.makedirs('_data')
except OSError:
  if not os.path.isdir('_data'):
    raise
file_name = '_data/categories.csv' if tag_or_category == 'category' else '_data/tags.csv'
file_exists = os.path.isfile(file_name)
data_categories = open(file_name, 'a')
# add the column heading if it the file was just created
if not file_exists:
  data_categories.write('slug,name\n')
string_to_write = slug + ',' + name + '\n'
# check that the category/tag hasn't been added yet
data_categories_read = open(file_name, 'r')
if not string_to_write in data_categories_read.read():
  data_categories.write(slug + ',' + name + '\n')

# create rss feed for the tag/category
if slug == 'podcast':
  sys.exit(0)
rss_feed = open('feed.' + tag_or_category + '.' + slug + '.xml', 'w')
rss_feed.write('---' + '\n')
rss_feed.write('layout: null' + '\n')
rss_feed.write('---' + '\n')
rss_feed.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
rss_feed.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">' + '\n')
rss_feed.write('  <channel>' + '\n')
rss_feed.write('    <title>{{ site.title | xml_escape }} - ' + name + '</title>' + '\n')
rss_feed.write('    <description>{{ site.description | xml_escape }}</description>' + '\n')
rss_feed.write('    <managingEditor>{{ site.author.email }}</managingEditor>' + '\n')
rss_feed.write('    <webMaster>{{ site.author.email }}</webMaster>' + '\n')
rss_feed.write('    <link>{{ site.url }}{{ site.baseurl }}/' + tag_or_category + '/' + slug + '/</link>' + '\n')
rss_feed.write('    <atom:link href="{{ "/feed.' + tag_or_category + '.' + slug +'.xml" | prepend: site.baseurl | prepend: site.url }}" rel="self" type="application/rss+xml"/>' + '\n')
rss_feed.write('    <pubDate>{{ site.time | date_to_rfc822 }}</pubDate>' + '\n')
rss_feed.write('    <lastBuildDate>{{ site.time | date_to_rfc822 }}</lastBuildDate>' + '\n')
rss_feed.write('    <generator>Jekyll v{{ jekyll.version }}</generator>' + '\n')
if tag_or_category == 'tag':
  rss_feed.write('    {% for post in site.tags.' + slug + ' limit:10 %}' + '\n')
elif tag_or_category == 'category':
  rss_feed.write('    {% for post in site.categories.' + slug +' limit:10 %}' + '\n')
rss_feed.write('      <item>' + '\n')
rss_feed.write('        <title>{{ post.title | xml_escape }}</title>' + '\n')
rss_feed.write('        <description>{{ post.content | xml_escape }}</description>' + '\n')
rss_feed.write('        <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>' + '\n')
rss_feed.write('        <link>{{ post.url | prepend: site.baseurl | prepend: site.url }}</link>' + '\n')
rss_feed.write('        <guid isPermaLink="true">{{ post.url | prepend: site.baseurl | prepend: site.url }}</guid>' + '\n')
rss_feed.write('        {% for tag in post.tags %}' + '\n')
rss_feed.write('        <category>{{ tag | xml_escape }}</category>' + '\n')
rss_feed.write('        {% endfor %}' + '\n')
rss_feed.write('        {% for cat in post.categories %}' + '\n')
rss_feed.write('        <category>{{ cat | xml_escape }}</category>' + '\n')
rss_feed.write('        {% endfor %}' + '\n')
rss_feed.write('      </item>' + '\n')
rss_feed.write('    {% endfor %}' + '\n')
rss_feed.write('  </channel>' + '\n')
rss_feed.write('</rss>' + '\n')
