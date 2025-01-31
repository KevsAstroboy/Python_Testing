from bs4 import BeautifulSoup


def test_show_summary_with_good_email(client):
    form_data = {'email': 'john@simplylift.co'}
    assertion_check = 'Welcome, Simply Lift'

    response = client.post('/showSummary', data=form_data)

    soup = BeautifulSoup(response.data, features='html.parser')
    soup_content = soup.find_all('h6')

    for content in soup_content:
        assert assertion_check in content.get_text()


def test_showsummary_with_bad_email(client):
    from_data = {'email': 'john@test.co'}
    assertion_check = "Cette adresse email n'existe pas."
    response = client.post('/showSummary', data=from_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h6")

    for content in soup_content:
        assert assertion_check in content.get_text()
