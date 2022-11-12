"""Tools for creating geohashes."""

import libgeohash
import shapely
from pystac import Item


def get_geohash(item: Item, precision: int = 4, invert_bbox: bool = False):
    """Return a geohash containing the STAC item's bounds."""
    bbox = item["bbox"]
    if invert_bbox:
        bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
        
    polygon = shapely.geometry.box(*bbox, ccw=True)
    longitude = polygon.centroid.coords.xy[0][0]
    latitude = polygon.centroid.coords.xy[1][0]

    geohash = pygeohash.encode(latitude=latitude, longitude=longitude, precision=precision)

    return geohash
