
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
