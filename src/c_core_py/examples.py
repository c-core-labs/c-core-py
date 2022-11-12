example_item_convergence = {
    "collection": "floe-edge",
    "stac_version": "1.0.0-beta.2",
    "id": "20201019T121115_20201025T121027_000025_fasticemotion",
    "assets": {
        "raster_tiles": {
            "title": "Raster tiles",
            "href": "https://c-core-ottawa.s3.amazonaws.com/tms/20201019T121115_20201025T121027_000025_fasticemotion-spo.tif/{z}/{x}/{y}.png",
        },
        "speckle_tracking": {
            "size": 15617254,
            "href": "https://s3.ca-central-1.amazonaws.com/c-core-ottawa/20201019T121115_20201025T121027_000025_fasticemotion-spo.tif",
        },
    },
    "type": "Feature",
    "links": [
        {
            "href": "https://s3.ca-central-1.amazonaws.com/c-core-catalog-dev/floe-edge/arctic/2020/20201019T121115_20201025T121027_000025_fasticemotion.json",
            "rel": "self",
        },
        {"rel": "parent", "href": "./../catalog.json"},
        {"href": "././../catalog.json", "rel": "collection"},
        {"href": "./././../catalog.json", "rel": "root"},
    ],
    "bbox": [
        -86.62753763168617,
        -72.93358927262537,
        69.62986045070944,
        73.72844542132746,
    ],
    "properties": {
        "ic:datetime_interval": "2020-10-19T12:11:15Z--2020-10-25T12:10:27Z",
        "rp:acquisition_time": None,
        "ic:datetime_start": "2020-10-19T12:11:15Z",
        "datetime": "2020-10-19T12:11:15Z",
        "rp:publish_time": "2020-10-28T16:01:43.236008",
        "ic:datetime_end": "2020-10-25T12:10:27Z",
        "ic:pair_id": 25,
    },
}
