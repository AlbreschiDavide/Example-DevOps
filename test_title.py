from app import get_title

def test_google():
    #arrange
    url = "https://www.google.com"
    #act
    result = get_title(url)
    #assert
    assert result == "Google"