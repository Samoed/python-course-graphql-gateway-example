from datetime import date, datetime

from services import CountriesService, NewsService, PlacesService


def test_read_news():
    news = NewsService.get_news()
    assert len(news) == 3
    assert news.keys() == {"ru", "ie", "rs"}
    ru_news = news["ru"]
    assert len(ru_news) == 4
    news_item = ru_news[0]
    assert news_item.author == "Спорт-Экспресс"
    assert news_item.source == "Google News"
    assert (
        news_item.title
        == "«Приходим с разминки перед «Амкалом» — а Овечкин уже «мертвый». Доктор дал ему нашатырь. А потом он ... - "
        "Спорт-Экспресс"
    )
    assert news_item.description is None
    assert (
        news_item.url
        == "https://news.google.com/rss/articles/CBMiyAFodHRwczovL3d3dy5zcG9ydC1leHByZXNzLnJ1L2Zvb3RiYWxsL3JmcGwvcmV2aW"
        "V3cy9pZ29yLWxlc2NodWstaW50ZXJ2eXUtdnJhdGFyeWEtbW9za292c2tvZ28tZGluYW1vLW9iLW92ZWNoa2luZS1yYWJvdGUtcy1jaGVyY2h"
        "lc292eW0tdnphaW1vb3Rub3NoZW5peWFoLXMtc2h1bmlueW0tcHJpa2x5dWNoZW5peWFoLXphaGFyeWFuYS0yMDQ1MjQwL9IBygFodHRwczo"
        "vL20uc3BvcnQtZXhwcmVzcy5ydS9mb290YmFsbC9yZnBsL3Jldmlld3MvaWdvci1sZXNjaHVrLWludGVydnl1LXZyYXRhcnlhLW1vc2tvdnN"
        "rb2dvLWRpbmFtby1vYi1vdmVjaGtpbmUtcmFib3RlLXMtY2hlcmNoZXNvdnltLXZ6YWltb290bm9zaGVuaXlhaC1zLXNodW5pbnltLXByaWt"
        "seXVjaGVuaXlhaC16YWhhcnlhbmEtMjA0NTI0MC9hbXAv?oc=5"
    )
    assert news_item.url_to_image is None
    assert news_item.published_at.replace(tzinfo=None) == datetime(2023, 3, 4, 8, 0, 1)
    assert news_item.content is None


def test_read_places():
    places = PlacesService.get_places()
    assert len(places) == 6

    place = places[0]
    assert place.id == 1
    assert place.city == "Perm"
    assert place.country == "RU"
    assert place.latitude == 58.0081
    assert place.longitude == 56.249
    assert place.locality == "Sverdlovsky City District"
    assert place.description == "Супер место!"
    assert place.created_at.date() == date(2022, 10, 29)
    assert place.created_at.date() == date(2022, 10, 29)


def test_read_place():
    place = PlacesService.get_place(1)
    assert place.id == 1
    assert place.city == "Perm"
    assert place.country == "RU"
    assert place.latitude == 58.0081
    assert place.longitude == 56.249
    assert place.locality == "Sverdlovsky City District"
    assert place.description == "Супер место!"
    assert place.created_at.date() == date(2022, 10, 29)
    assert place.created_at.date() == date(2022, 10, 29)


def test_read_countries():
    countries = CountriesService.get_countries()
    assert len(countries) == 4

    country = countries[1]
    assert country.name == "Russian Federation"
    assert country.alpha2code == "RU"
    assert country.alpha3code == "RUS"
    assert country.capital == "Moscow"
    assert country.region == "Europe"
    assert country.subregion == "Eastern Europe"
    assert country.population == 146599183
    assert country.latitude == 60.0
    assert country.longitude == 100.0
    assert country.demonym == "Russian"
    assert country.area == 17124442.0
    assert country.numeric_code == 643
    assert country.flag == "http://assets.promptapi.com/flags/RU.svg"
    assert country.currencies == ["RUB"]
    assert country.languages == ["Russian"]
