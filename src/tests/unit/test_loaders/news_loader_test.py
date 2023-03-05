from datetime import datetime

import pytest

from dataloaders import NewsLoader
from models.news import NewsModel


class TestNewsLoader:
    @pytest.fixture
    def loader(self):
        return NewsLoader()

    def test_load_one_news(self, loader):
        news: list[NewsModel] = loader.load("RU").get()

        assert len(news) == 4
        news_item = news[0]
        assert news_item.author == "Спорт-Экспресс"
        assert news_item.source == "Google News"
        assert (
            news_item.title
            == "«Приходим с разминки перед «Амкалом» — а Овечкин уже «мертвый». Доктор дал ему нашатырь."
            " А потом он ... - Спорт-Экспресс"
        )
        assert news_item.description is None
        assert (
            news_item.url == "https://news.google.com/rss/articles/"
            "CBMiyAFodHRwczovL3d3dy5zcG9ydC1leHByZXNzLnJ1L2Zvb3RiYWxsL3JmcGwvcmV2aWV3cy9pZ29yLWxlc2NodWstaW50ZXJ2eXUtdn"
            "JhdGFyeWEtbW9za292c2tvZ28tZGluYW1vLW9iLW92ZWNoa2luZS1yYWJvdGUtcy1jaGVyY2hlc292eW0tdnphaW1vb3Rub3NoZW5peWFo"
            "LXMtc2h1bmlueW0tcHJpa2x5dWNoZW5peWFoLXphaGFyeWFuYS0yMDQ1MjQwL9IBygFodHRwczovL20uc3BvcnQtZXhwcmVzcy5ydS9mb2"
            "90YmFsbC9yZnBsL3Jldmlld3MvaWdvci1sZXNjaHVrLWludGVydnl1LXZyYXRhcnlhLW1vc2tvdnNrb2dvLWRpbmFtby1vYi1vdmVjaGtp"
            "bmUtcmFib3RlLXMtY2hlcmNoZXNvdnltLXZ6YWltb290bm9zaGVuaXlhaC1zLXNodW5pbnltLXByaWtseXVjaGVuaXlhaC16YWhhcnlhbm"
            "EtMjA0NTI0MC9hbXAv?oc=5"
        )
        assert news_item.url_to_image is None
        assert news_item.published_at.replace(tzinfo=None) == datetime(
            2023, 3, 4, 8, 0, 1
        )
        assert news_item.content is None

    def test_load_many_news(self, loader):
        news: list[list[NewsModel]] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(news) == 3
