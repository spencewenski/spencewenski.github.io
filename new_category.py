"""
Usage: new_category <tag|category> <slug> <name>
"""

import sys, os.path

tag_or_category = sys.argv[1] if len(sys.argv) > 1 else '';
slug = sys.argv[2] if len(sys.argv) > 2 else '';
name = sys.argv[3] if len(sys.argv) > 3 else '';

if slug == '' or name == '':
  print __doc__
  sys.exit(0)

# create tag/category dir, then create tag/category page
if not os.path.exists(tag_or_category):
  os.makedirs(tag_or_category)
category_page = open(tag_or_category +'/' + slug + '.md', 'w')
category_page.write('---\n')
category_page.write('layout: blog_by_' + tag_or_category + '\n')
category_page.write(tag_or_category + ': ' + slug + '\n')
category_page.write('permalink: ' + tag_or_category + '/' + slug + '/\n')
category_page.write('---\n')

# create _data/categories if it doesn't exist, then append category to the list
if not os.path.exists('_data'):
  os.makedirs('_data')
file_name = '_data/categories.csv' if tag_or_category == 'category' else '_data/tags.csv'
file_exists = os.path.isfile(file_name)
data_categories = open(file_name, 'a')
if not file_exists:
  data_categories.write('slug,name\n')
data_categories.write(slug + ',' + name + '\n')
