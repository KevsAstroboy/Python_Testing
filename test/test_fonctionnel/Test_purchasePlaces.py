from bs4 import BeautifulSoup


def test_purchase_places_when_is_empty(client):
    from_data = {'places': ''}
    assertion_check = "Veuillez bien renseigner le " \
                      "nombre de place que vous voulez réserver"
    response = client.post('/purchasePlaces', data=from_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h6")
    for content in soup_content:
        assert assertion_check in content.get_text()


def test_purchase_places_when_is_more_than_twelve(client):
    from_data = {'places': 12}
    assertion_check = "Impossible de réserver plus de 12 places à la fois."
    response = client.post('/purchasePlaces', data=from_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h6")
    for content in soup_content:
        assert assertion_check in content.get_text()
