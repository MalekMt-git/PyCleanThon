from flask import Flask, render_template

from data.api.ArtObjectAPIService import ArtObjectAPIService
from data.repository.ArtObjectRepositoryImpl import ArtObjectRepositoryImpl
from domain.model.ArtObjectHeadlinesQuery import ArtObjectHeadlinesQuery

app = Flask(__name__)


@app.route("/")
def hello_world():
    repository = ArtObjectRepositoryImpl(ArtObjectAPIService())
    art_objects = repository.get_art_objects(ArtObjectHeadlinesQuery("en", 50, 1))
    return render_template("rijksmuseum/home.html", data=art_objects)


if __name__ == '__main__':
    app.run(debug=True)
