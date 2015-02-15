import sys

tag_or_category = sys.argv[1] if len(sys.argv) > 1 else '';
slug = sys.argv[2] if len(sys.argv) > 2 else '';
name = sys.argv[3] if len(sys.argv) > 3 else '';

if slug == '' or name == '':
  print 'usage: ' + sys.argv[0] + '[tag|category] <slug> <name>'
  sys.exit(0)

# write category page
category_page = open(tag_or_category +'/' + slug + '.md', 'w')
category_page.write('---\n')
category_page.write('layout: blog_by_' + tag_or_category + '\n')
category_page.write(tag_or_category + ': ' + slug + '\n')
category_page.write('permalink: ' + tag_or_category + '/' + slug + '/\n')
category_page.write('---\n')

# append category to _data/categories
data_categories = open('_data/categories.csv', 'a') if tag_or_category == 'category' else open('_data/tags.csv', 'a')
data_categories.write(slug + ',' + name + '\n')
