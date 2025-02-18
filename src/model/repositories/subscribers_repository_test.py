import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {"name": "Willian",
                       "email": "H4l0t@example.com",
                        "link": "meulink.com",
                        "evento_id": 1}

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "H4l0t@example.com"
    evento_id = 1
    
    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)