import urllib.request, json

from .models import Article,Source
# "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3c9d1cfa248042a39c0cf9008021a9ac"
api_key = None
base_article_url = None
base_source_url = None

def configure_request(app):
	global api_key, base_article_url,base_source_url
	api_key = app.config['NEWS_API_KEY']
	base_article_url = app.config['NEWS_API_BASE_URL']
	base_source_url = app.config['NEWS_SOURCES_BASE_URL']

# def get_news(country,category):
# 	get_news_url = base_article_url.format(country,category,api_key)

# 	all_data = []

# 	with urllib.request.urlopen(get_news_url) as url:
# 		bytes = url.read()
# 		mydict = json.loads(bytes)
# 		articles = mydict['articles']

# 		for article in articles:
# 			id = article["source"]["id"]
# 			name = article["source"]["name"]
# 			author = article["author"]
# 			title = article["title"]
# 			description = article["description"]
# 			url = article["url"]
# 			image = article["urlToImage"]
# 			published = article["publishedAt"]

# 			all_data.append(Article(id,name,author,title,description,url,image,published))
# 	return all_data

def get_source():
	get_sources_url = base_source_url.format(api_key)
	all_data = []

	with urllib.request.urlopen(get_sources_url) as url:
		bytes = url.read()
		mydict = json.loads(bytes)

		sources = mydict['sources']

		for source in sources:
			id = source['id']
			name= source['name']
			description = source['description']
			url = source['url']
			category = source['category']
			language = source['language']
			country = source['country']

			all_data.append(Source(id,name,description,url,category,language,country))
	return all_data


def get_news(country,category):
	get_news_url = base_article_url.format(country,category,api_key)
	all_data=[]

	articles = [{

'source': {'id': 'business-insider', 'name': 'Business Insider'}, 'author': None, 'title': 'NVIDIA WARNS: We are going to see a big drop in crypto revenue', 'description': None, 'url': 'http://www.businessinsider.com/nvidia-stock-price-crypto-revenues-going-to-see-big-drop-2018-5', 'urlToImage': None, 'publishedAt': '2018-05-11T12:48:29Z'

}, 
 {'source': {'id': None, 'name': 'Npr.org'}, 'author': 'James Doubek', 'title': "Starbucks Will 'Give People The Key' To Bathroom Regardless Of Purchase", 'description': 'Starbucks Chairman Howard Schultz said the company will let everyone use its bathrooms, whether they bought a drink or not. It comes after the arrest of two black men at a Philadelphia location.', 'url': 'https://www.npr.org/sections/thetwo-way/2018/05/11/610337214/starbucks-will-give-people-the-key-to-restroom-regardless-of-purchase-ceo-says', 'urlToImage': 'https://media.npr.org/assets/img/2018/05/11/gettyimages-957041738_wide-7d7447d982f7f1c02ef46afb1f67619933744184.jpg?s=1400', 'publishedAt': '2018-05-11T12:06:52Z'}, 


 {'source': {'id': 'reuters', 'name': 'Reuters'}, 'author': 'Reuters Editorial', 'title': 'Symantec shares set for worst fall in 17 years', 'description': "Symantec Corp's (SYMC.O) shares sank as much as 25 percent on Friday after the cyber-security firm said it was investigating concerns raised by a former employee but gave little other detail, puzzling investors and Wall Street analysts.", 'url': 'https://www.reuters.com/article/us-symantec-research/symantec-shares-set-for-worst-fall-in-17-years-idUSKBN1IC1AW', 'urlToImage': 'https://s1.reutersmedia.net/resources/r/?m=02&d=20180511&t=2&i=1260921381&w=1200&r=LYNXMPEE4A0S0', 'publishedAt': '2018-05-11T11:54:32Z'}, 

 {'source': {'id': 'the-verge', 'name': 'The Verge'}, 'author': 'Thuy Ong', 'title': "Elon Musk plans to offer free test rides through LA tunnel 'in a few months'", 'description': 'Pending regulatory approval, of course', 'url': 'https://www.theverge.com/2018/5/11/17343530/elon-musk-free-test-rides-boring-company-la-tunnel', 'urlToImage': 'https://cdn.vox-cdn.com/thumbor/_U2ZOQa12SwYqJL78I_MMQBOD90=/0x405:1000x929/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/10821017/Hawthorne_Tunnel_10.28.17.jpeg', 'publishedAt': '2018-05-11T11:54:00Z'}, {'source': {'id': 'fortune', 'name': 'Fortune'}, 'author': 'David Meyer', 'title': "Watch Boston Dynamics' Atlas and SpotMini Robots Run and Navigate Themselves", 'description': '', 'url': 'http://fortune.com/2018/05/11/boston-dynamics-atlas-spotmini-run/', 'urlToImage': 'https://fortunedotcom.files.wordpress.com/2018/05/atlas.jpg', 'publishedAt': '2018-05-11T11:34:14Z'}, {'source': {'id': 'the-wall-street-journal', 'name': 'The Wall Street Journal'}, 'author': 'Ben Dummett', 'title': 'Buyout Giant Silver Lake Jumps Into UK Digital Property Search Market', 'description': 'Silver Lake\xa0struck a $2.98 billion deal to acquire one of Britain’s biggest internet property search companies, a bet on the increasing use of the web by consumers and real-estate agents.', 'url': 'https://www.wsj.com/articles/buyout-giant-silver-lake-jumps-into-u-k-digital-property-search-market-1526037471', 'urlToImage': 'https://images.wsj.net/im-10256/social', 'publishedAt': '2018-05-11T11:21:40Z'}, {'source': {'id': 'bloomberg', 'name': 'Bloomberg'}, 'author': 'Stephen Morris, John Glover', 'title': 'Barclays CEO Fined About $870000 on Whistle-Blower Incident', 'description': 'Barclays Plc Chief Executive Officer Jes Staley was fined 642,430 pounds ($870,557) by British regulators for his attempts to uncover a whistle-blower.', 'url': 'https://www.bloomberg.com/news/articles/2018-05-11/barclays-ceo-staley-fined-about-870-000-by-british-regulators', 'urlToImage': 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ivnQQaRDPFZ0/v0/1200x800.jpg', 'publishedAt': '2018-05-11T10:48:24Z'}, {'source': {'id': 'bloomberg', 'name': 'Bloomberg'}, 'author': 'Shinhye Kang, Heejin Kim', 'title': 'Cryptocurrency Exchange Upbit Raided by Korean Authorities', 'description': 'South Korean prosecutors raided the offices of Upbit, one of the world’s largest cryptocurrency exchanges.', 'url': 'https://www.bloomberg.com/news/articles/2018-05-11/cryptocurrency-exchange-upbit-raided-by-south-korean-authorities', 'urlToImage': 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iTwJRKZFPhwM/v0/1200x819.jpg', 'publishedAt': '2018-05-11T10:22:40Z'}, {'source': {'id': 'the-wall-street-journal', 'name': 'The Wall Street Journal'}, 'author': 'Sam Schechner', 'title': 'Stage Is Set for Battle Over Data Privacy in Europe', 'description': 'A battle is looming in Europe over what information Facebook, Google and other companies can demand from you. It boils down to what they really need to know—a debate that could end up in courts for years.', 'url': 'https://www.wsj.com/articles/stage-is-set-for-battle-over-data-privacy-in-europe-1526031104', 'urlToImage': 'https://images.wsj.net/im-9996/social', 'publishedAt': '2018-05-11T09:34:38Z'}, {'source': {'id': 'business-insider', 'name': 'Business Insider'}, 'author': 'Reuters', 'title': 'US sanctions cause Kremlin-linked Russian tycoon to have to give up his private jets', 'description': 'Deripaska was included on a U.S. sanctions blacklist on April 6 because, officials in Washington said, he and other Russian oligarchs had profited from the "mal', 'url': 'http://www.businessinsider.com/us-sanctions-cause-russian-tycoon-oleg-deripaska-to-lose-private-jets-2018-5', 'urlToImage': 'https://amp.businessinsider.com/images/5af5562b1ae5f31c008b4812-640-320.jpg', 'publishedAt': '2018-05-11T08:46:59Z'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Jethro Mullen', 'title': 'Cisco has yanked all its ads from YouTube', 'description': "Cisco, one of America's biggest tech companies, has stopped running ads on YouTube after some of them appeared on channels promoting extremist content.", 'url': 'http://money.cnn.com/2018/05/11/technology/cisco-youtube-no-ads/index.html', 'urlToImage': 'http://i2.cdn.turner.com/money/dam/assets/180419124058-youtube-ads-extreme-content-780x439.jpg', 'publishedAt': '2018-05-11T06:25:00Z'}, {'source': {'id': None, 'name': 'Marketwatch.com'}, 'author': 'Max A. Cherney', 'title': 'Trade Desk stock skyrockets as ad spending on streaming TV goes up 2000%', 'description': 'The Trade Desk Inc. walloped earnings expectations in a report Thursday thanks to huge gains for advertising on streaming-video services, sending the stock up 22% in after-hours trading.', 'url': 'https://www.marketwatch.com/story/trade-desk-stock-skyrockets-as-ad-spending-on-streaming-tv-goes-up-2000-2018-05-10', 'urlToImage': 'http://s.marketwatch.com/public/resources/MWimages/MW-GJ020_traded_ZG_20180510185205.jpg', 'publishedAt': '2018-05-11T00:42:09Z'}, {'source': {'id': None, 'name': 'Yahoo.com'}, 'author': None, 'title': 'News Corp reports loss on writedowns, weakness in newspapers', 'description': "Rupert Murdoch's newspaper-focused News Corp on Thursday reported a loss in the past quarter, as results were hit by a writedown in the value of its Australian television operations and declines in print advertising revenues.", 'url': 'https://au.news.yahoo.com/news-corp-reports-loss-writedowns-weakness-newspapers-003155123--spt.html', 'urlToImage': 'https://s.yimg.com/uu/api/res/1.2/Epfnmxh2xSGg3A6HSDiSZg--~B/aD0zNDE7dz01MTI7c209MTthcHBpZD15dGFjaHlvbg--/http://media.zenfs.com/en_AU/Sports/Agence-FrancePresse/cddd974e01d272036ac727c98da45091c4e95467.jpg', 'publishedAt': '2018-05-11T00:40:13Z'}, {'source': {'id': None, 'name': 'Qz.com'}, 'author': 'Alison Griswold', 'title': "Wall Street is so sure MoviePass will fail, it's become incredibly expensive to short", 'description': "If a movie a day for $10 a month seemed too good to be true, that's probably because it was.", 'url': 'https://qz.com/1269930/moviepass-parent-helios-and-matheson-hmny-is-incredibly-expensive-to-short/', 'urlToImage': 'https://qz.com/wp-content/uploads/2018/05/moviepass-card-e1525977624325.jpg?quality=80&strip=all&w=1600', 'publishedAt': '2018-05-10T19:53:17Z'}, {'source': {'id': None, 'name': 'Npr.org'}, 'author': 'Laurel Wamsley', 'title': 'Man Allegedly Used Change Of Address Form To Move UPS Headquarters To His Apartment', 'description': 'Prosecutors say he received thousands of pieces of mail intended for the company, including checks and corporate credit cards. He is now facing federal charges.', 'url': 'https://www.npr.org/sections/thetwo-way/2018/05/10/610102872/man-allegedly-used-change-of-address-form-to-move-ups-headquarters-to-his-apartm', 'urlToImage': 'https://media.npr.org/assets/img/2018/05/10/gettyimages-72846750_wide-5c765271a209872860edbe2a65f38cb7307c9b1f.jpg?s=1400', 'publishedAt': '2018-05-10T19:25:42Z'}, {'source': {'id': None, 'name': 'Forbes.com'}, 'author': 'Darren Heitner', 'title': 'Skechers Says In New Lawsuit It Was Harmed By Adidas Paying Players Under The Table', 'description': 'Skechers has filed a federal civil court complaint against its competitor adidas based on grounds that it has suffered due to adidas allegedly illegally paying players under the table.', 'url': 'https://www.forbes.com/sites/darrenheitner/2018/05/10/skechers-says-it-was-harmed-by-adidas-paying-players-under-the-table-in-new-lawsuit/', 'urlToImage': 'https://thumbor.forbes.com/thumbor/600x315/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F950414064%2F960x0.jpg%3Ffit%3Dscale', 'publishedAt': '2018-05-10T19:17:49Z'}, {'source': {'id': None, 'name': 'Chicagotribune.com'}, 'author': 'Tom Krisher', 'title': 'Parts shortage that hit Ford spreads to more companies', 'description': 'Ford was forced to temporarily halt production of its popular F-150 pickup truck Wednesday after a fire at a supplier last week caused a parts shortage.', 'url': 'http://www.chicagotribune.com/business/ct-ford-suspends-f-150-production-20180510-story.html', 'urlToImage': 'http://www.trbimg.com/img-5af489c5/turbine/ct-ford-suspends-f-150-production-20180510', 'publishedAt': '2018-05-10T18:04:00Z'}, {'source': {'id': 'the-washington-post', 'name': 'The Washington Post'}, 'author': None, 'title': 'Florida man behind 100 million robocalls hit with huge FCC fine', 'description': 'Adrian Ambramovich is fined $120 million for scheme the FCC said posed a financial and public safety threat', 'url': 'https://www.washingtonpost.com/news/business/wp/2018/05/10/florida-man-behind-100-million-robocalls-hit-with-huge-fcc-fine/', 'urlToImage': 'https://www.washingtonpost.com/resizer/Q3jxkHDeHSObyTIpbRM3xB7GgRw=/1484x0/arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/HDMIWE7CPE26DHSAA446CN34XE.jpg', 'publishedAt': '2018-05-10T15:51:15Z'}, {'source': {'id': 'the-wall-street-journal', 'name': 'The Wall Street Journal'}, 'author': 'Michael Wursthorn', 'title': 'US Stocks Climb as Inflation Fears, Volatility Ebb', 'description': 'U.S. stocks rose and market volatility continued to fade, as fears of runaway inflation abated to help send the Dow Jones Industrial Average higher for a sixth consecutive session.', 'url': 'https://www.wsj.com/articles/asian-stocks-broadly-rise-but-pain-looms-in-malaysia-1525919676', 'urlToImage': 'https://images.wsj.net/im-10134/social', 'publishedAt': '2018-05-10T13:56:00Z'}, {'source': {'id': 'techcrunch', 'name': 'TechCrunch'}, 'author': 'Matthew Lynley', 'title': 'Free stock trading app Robinhood rockets to a $5.6B valuation with new funding round', 'description': 'Robinhood started off as a dead-simple stock trading application that had no transaction fees —\xa0but since it’s continued to grow, and especially as it starts to dive into cryptocurrency, investors are getting pretty excited about its prospects and are pouring…', 'url': 'https://techcrunch.com/2018/05/10/robinhood-rockets-to-a-5-6b-valuation-with-a-massive-new-funding-round/', 'urlToImage': 'https://techcrunch.com/wp-content/uploads/2018/05/vlad-tenev.jpg?w=599', 'publishedAt': '2018-05-10T13:01:05Z'}]

	for article in articles:
		id = article["source"]["id"]
		name = article["source"]["name"]
		author = article["author"]
		title = article["title"]
		description = article["description"]
		url = article["url"]
		image = article["urlToImage"]
		published = article["publishedAt"]

		all_data.append(Article(id,name,author,title,description,url,image,published))
	return all_data