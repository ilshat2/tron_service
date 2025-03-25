from tronpy import Tron
from tronpy.providers import HTTPProvider


def get_tron_wallet_info(address: str):
    client = Tron(HTTPProvider("https://api.trongrid.io"))

    try:
        account = client.get_account(address)
        balance = client.get_account_balance(address)

        return {
            "balance": balance,
            "bandwidth": account.get('free_net_usage', 0),
            "energy": account.get('account_resource', {}).get('energy_usage', 0)
        }
    except Exception as e:
        raise ValueError(f"Invalid Tron address: {str(e)}")
