from flask import render_template
from . import main
from ..requests import get_news,get_source





@main.route("/")
def index():
	return render_template("index.html")



@main.route("/country/<string:country>")
def article(country):
	display = country
	business = get_news(country,'business')
	sports= get_news(country,'sports')
	entertainment= get_news(country,'entertainment')
	general = get_news(country,'general')
	health = get_news(country,'health')
	science = get_news(country,'science')
	technology = get_news(country,'technology')


	return render_template("article.html", country=country,business=business,sports=sports,entertainment=entertainment,general=general,health=health,science=science,technology=technology)

@main.route("/sources")
def sources():
	sources = get_source()
	print(sources)

	return render_template("article.html", sources=sources)

