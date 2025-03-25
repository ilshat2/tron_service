from unittest.mock import patch


def test_wallet_info_endpoint(client, db):
    with patch('app.utils.get_tron_wallet_info') as mock_tron:
        mock_tron.return_value = {
            "balance": 100.0,
            "bandwidth": 500,
            "energy": 200
        }

        response = client.post(
            "/wallet/",
            json={"wallet_address": "TX111...111"}
        )

        assert response.status_code == 200
        assert response.json()["balance"] == 100.0


def test_get_requests_endpoint(client, db):
    # Сначала создаем запись
    client.post("/wallet/", json={"wallet_address": "TX111...111"})

    # Проверяем пагинацию
    response = client.get("/requests/?skip=0&limit=1")
    assert len(response.json()) == 1
    assert response.json()[0]["wallet_address"] == "TX111...111"
