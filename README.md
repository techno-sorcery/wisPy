---
title: wisPy
author: Hayden Buscher
description: A dead-simple static site generator, for those who want nothing more than to convert markdown to html.
lastmod: 2023-02-14
---

### Website Interpreter, Static aka wisPy  
**Links**  
[Github repo](https://github.com/techno-sorcery/wisPy)

**Description**  
wisPy is a dead-simple static site generator, for those want nothing more than to convert markdown to html. While full CMSs have lots of useful features, many go unused with simpler websites. This adds unnecessary complexity to otherwise straight-forward projects. 

wisPy is different- all it does is scrape markdown files from any number of input folders, apply the specified themes, and dump the resulting html files into any number of output folders. It can also parse YAML-style metadata into corresponding title/meta tags, and generate xml sitemaps.

If you'd like to see what wisPy can do, well... I use it to generate most of this site's content.<br><br>

**Config System**  
Parameters are defined in the wispy_config.ini file, in groups known as "tags". Regular tags operate within the scope of a single folder, but parameters can also be defined globally with the "global" tag. An example of my site's config file is below:

<pre>
# Define global params
[global]
root =          ..
template =      ../global/template.html
suffix =        &nbsp— Techno-Sorcery
sitemap =       true
url =           https://techno-sorcery.com
css =           /global/css/main.css /global/css/responsive.css

# Define local params
[main]
input =     ../main/md
output =    ../main
priority =  1
</pre>

Any number of tags can be included in the same file. The only necessary parameter is "input"; you are not required to specify an output folder, template, or suffix.

Below is a full list of wisPy-supported parameters:
<pre>
root            root directory for sitemap, defined globally
input           input folder, containing markdown
output          output folder, where html is stored
template        path to html template

sitemap         if "true", pages are added to sitemap.xml
url             base site url, begins with "http://"
lastmod         date of last modification, yyyy-mm-dd
priority        web-crawler priority
changefreq      web-crawler page change frequency

draft           if "true", page isn't compiled

prefix          title prefix
suffix          title suffix
title           page title

gentag          if false, doesn't inject wisPy version tag
author          author, meta tag
date            date published, meta tag, yyyy-mm-dd
keywords        page keywords, meta tag
description     page description, meta tag
viewport        viewport properties, meta tag

css             stylesheet paths, separated by whitespace
</pre>

Parameters can be defined per-file, within a YAML-style metadata header. Note that these headers are of a proprietary format, custom to wisPy. Below is an example of this page's header:

<pre>
———
title: wisPy
author: Hayden Buscher
description: A dead-simple static site generator, for those who want nothing more than to convert markdown to html.
lastmod: 2023-02-14
———
</pre>

Note that metadata overrides local definitions, and local definitions override global ones. Through this system, you can exercise a great deal of flexibility.<br><br>

**Templates**  
Unlike other site generators, wisPy uses vanilla html files as templates. First, it looks for a <!––HEAD––> tag in the head to begin inserting metadata. Then, it looks for a an <!––INSERT––> tag in the body before writing the converted html. Everything within the template is preserved, including style and script tags.
<br><br>

**Sitemaps**  
Generating sitemaps with wisPy is easy. Simply define a base url and root folder in the config, and mark whichever pages you want to index with "sitemap = true". wisPy sitemaps are in the XML format for maximum compatibility, and can include a variety of directives.<br><br>

**Plans**  
wisPy will never become a content management system, that goes against its philosophy. However, features will be added if they're high in utility without adding much size to the codebase. One such thing in the works is table of contents generation. Soon, wisPy should be able to give you page, folder, and site-wide tables of contents based on metadata.

