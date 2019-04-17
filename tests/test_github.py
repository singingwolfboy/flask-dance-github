def test_index_authorized(app):
    with app.test_client() as client:
        response = client.get("/", base_url="https://example.com")

    assert response.status_code == 200
    text = response.get_data(as_text=True)
    assert text == "You are @singingwolfboy on GitHub"
