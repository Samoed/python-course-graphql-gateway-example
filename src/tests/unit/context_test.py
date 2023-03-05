from context import get_context, register_dataloaders
from dataloaders import CountryLoader, NewsLoader


def test_register_dataloaders():
    dataloaders = register_dataloaders()
    assert len(dataloaders) == 2
    assert dataloaders.keys() == {"countries", "news"}
    assert isinstance(dataloaders["countries"], CountryLoader)
    assert isinstance(dataloaders["news"], NewsLoader)


def test_get_context():
    context = get_context()
    assert len(context) == 1
    assert context.keys() == {"dataloaders"}
    assert isinstance(context["dataloaders"], dict)
    assert len(context["dataloaders"]) == 2
    assert context["dataloaders"].keys() == {"countries", "news"}
    assert isinstance(context["dataloaders"]["countries"], CountryLoader)
    assert isinstance(context["dataloaders"]["news"], NewsLoader)
