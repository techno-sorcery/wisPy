## Website Interpreter, Static aka wisPy
wisPy is a dead-simple static site generator, for those want nothing more than to convert markdown to html. While full CMSs have lots of useful features, many go unused with simpler wesites. This adds unneccessary complexity to otherwise straight-forward projects. 

wisPy is different- all it does is scrape markdown files from any number of input folders, apply the specified themes, and dump the resulting html files into any number of output folders. That's it. It can also parse integrated YAML metadata, and generate corresponding title/meta tags.

If you'd like to see what wisPy can do, just check out [my website](http://techno-sorcery.com); I use it to generate most of my page content.

## Config System
wisPy config files are structured thusly:
```
[blog]                                  group
input =       blogposts/md              input folder, containing markdown files
output =      blogposts                 output folder, where html is stored
template =    blogposts/template.html   path to html template
suffix =      &nbsp- My Blog            optional page title suffix
```
Note that any number of groups can be included in the same file. The only necessary parameter is "input"; you are not required to specify an output folder, template, or suffix.

## Plans
wisPy will never become a content management system, that defeats its entire point. However, I'm open to the addition of some basic features. For instance, one feature that's currently in progress is table-of-contents generation.
