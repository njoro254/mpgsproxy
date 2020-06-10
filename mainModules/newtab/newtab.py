import webbrowser

@app.route('/test')
def my_page():
    return webbrowser.open_new_tab('http://mylink.com')


<a href="http://mylink.com" target="_blank">Link</a>