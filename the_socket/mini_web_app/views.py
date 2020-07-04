def index():
    with open('the_socket/mini_web_app/templates/index.html') as templates:
        return templates.read()

def blog():
    with open('the_socket/mini_web_app/templates/blog.html') as templates:
        return templates.read()