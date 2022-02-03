

template = open('template/template.html').read()

html = open('content/blog/posts/first.md').read()

html = "<main>" + html + "</main>"

template = template.replace("{{body}}", html)
template = template.replace("{{display}}", "")

f = open("blog/index.html", 'w')
f.write(template)
