"""Tools for creating geohashes."""

from typing import Optional
import libgeohash
import shapely
from pystac import Item
import google.cloud
from google.cloud import firestore

from c_core_py.firestore import get_document, set_document


def get_geohash(item: Item, precision: int = 4, invert_bbox: bool = False):
    """Return a geohash containing the STAC item's bounds."""
    bbox = item["bbox"]
    if invert_bbox:
        bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]

    polygon = shapely.geometry.box(*bbox, ccw=True)
    longitude = polygon.centroid.coords.xy[0][0]
    latitude = polygon.centroid.coords.xy[1][0]

    geohash = libgeohash.encode(lat=latitude, lon=longitude, precision=precision)

    return geohash


def get_geohash_bounds(geohash):
    """Return the bounds of a geohash."""
    polygon = libgeohash.geohash_to_polygon([geohash])
    bounds = polygon.bounds

    return bounds


def update_geohash_index(
    item: Item,
    collection: str,
    db: google.cloud.firestore_v1.client.Client,
    *,
    index_collection: Optional[str] = None,
    datetime_property: str = "datetime",
    precision: int = 4,
    invert_bbox: bool = False,
):
    """Update database with new item's geohash and date."""
    if not index_collection:
        index_collection = f"{collection}-index"

    geohash = get_geohash(item, precision=precision, invert_bbox=invert_bbox)
    datetime_string = item["properties"][datetime_property]
    date = datetime_string.split("T")[0]
    geohash_bounds = get_geohash_bounds(geohash)

    # Get geohash index
    document_index = get_document(
        document_id=geohash, collection_id=index_collection, db=db
    )

    # Create or update geohash index
    if not document_index:
        document_index = {
            "id": geohash,
            "bbox": geohash_bounds,
            "properties": {
                date: 1,
            },
        }
    else:
        if not date in document_index["properties"].keys():
            document_index["properties"][date] = 1
        else:
            document_index["properties"][date] = document_index["properties"][date] + 1

    # Set geohash index
    set_document(
        document_id=geohash,
        document=document_index,
        collection_id=index_collection,
        db=db,
    )

    return document_index
