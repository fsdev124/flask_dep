from dep_app import create_app
from flask import render_template

app = create_app()

@app.errorhandler(500)
@app.errorhandler(Exception)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 500

if __name__ == '__main__':
    app.run(debug=True)