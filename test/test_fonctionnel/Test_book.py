from bs4 import BeautifulSoup
import json



def test_booking_with_good_url(client):
    assertion_check = 'Welcome to the Spring Festival'
    response = client.get('/book/Spring Festival/Simply Lift')

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h2")

    for content in soup_content:
        assert assertion_check in content.get_text()



def test_booking_with_bad_url(client):
    assertion_check = "Quelque chose s'est mal passé , veuillez réessayer"
    response = client.get('/book/Spring/Simply Lift')

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h6")

    for content in soup_content:
        assert assertion_check in content.get_text()
