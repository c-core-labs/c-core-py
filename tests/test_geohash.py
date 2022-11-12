from google.cloud import firestore

from c_core_py.geohash import get_geohash, update_geohash_index
from c_core_py.examples import example_item_convergence
from c_core_py.firestore import get_document


db = firestore.Client.from_service_account_json("credentials.json")


def test_get_geohash():
    geohash = get_geohash(example_item_convergence)

    assert geohash == "eb1f"


def test_update_geohash_index():
    collection = "test"
    collection_index = "test-index"
    date = example_item_convergence["properties"]["datetime"].split("T")[0]
    
    result = update_geohash_index(example_item_convergence, "test", db=db)
    geohash = result["id"]

    assert geohash== "eb1f"
    
    document_index = get_document(document_id=geohash, collection_id=collection_index, db=db)

    assert document_index["properties"][date] > 0
