"""Utility functions for Firestore databases."""

import google.cloud


def get_document(
    document_id: str,
    collection_id: str,
    *,
    db: google.cloud.firestore_v1.client.Client,
):
    """Get a snapshot and return the document."""
    document_reference = db.collection(collection_id).document(document_id)
    document_snapshot = document_reference.get()
    document = document_snapshot.to_dict()

    return document


def set_document(
    document_id: str,
    document: dict,
    collection_id: str,
    *,
    merge: bool = True,
    db: google.cloud.firestore_v1.client.Client,
):
    """Set document in Firestore collection."""
    document_id_string = str(document_id)
    document_reference = db.collection(collection_id).document(document_id_string)

    document_reference.set(document, merge=merge)

    return document_id_string
