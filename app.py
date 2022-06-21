from flask import Flask
from data.api.ArtObjectAPIService import ArtObjectAPIService
from data.repository.ArtObjectRepositoryImpl import ArtObjectRepositoryImpl
from domain.model.ArtObjectHeadlinesQuery import ArtObjectHeadlinesQuery

app = Flask(__name__)


@app.route("/")
def hello_world():
    repository = ArtObjectRepositoryImpl(ArtObjectAPIService())
    api_response = repository.get_art_objects(ArtObjectHeadlinesQuery("en", 5, 1)).to_dict()
    return api_response


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(debug=True)
