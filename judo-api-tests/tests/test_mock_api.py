from judo import Judo


def test_get_user_from_mock_server():
    judo = Judo()
    port = 8099

    mock = judo.start_mock(port=port)
    try:
        mock.when("GET", "/users/1").then(
            status=200,
            json={"id": 1, "name": "Ada Lovelace", "role": "admin"},
        )

        response = judo.get(f"http://localhost:{port}/users/1")

        judo.match(response.status_code, 200)
        judo.match(response.json["name"], "Ada Lovelace")
        judo.match(response.json["role"], "admin")
    finally:
        judo.stop_mock()
