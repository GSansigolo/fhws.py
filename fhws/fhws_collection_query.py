def collection_query(collection, start_date, end_date, tile=None, bbox=None, freq=None, bands=None):
    """An object that contains the information associated with a collection 
    that can be downloaded or acessed.

    Args:
        collection : String containing a collection id.

        start_date String containing the start date of the associated collection. Following YYYY-MM-DD structure.

        end_date : String containing the start date of the associated collection. Following YYYY-MM-DD structure.

        freq : Optional, string containing the frequency of images of the associated collection. Following (days)D structure. 

        bands : Optional, string containing the list bands id.
    """

    return dict(
        collection = collection,
        bands = bands,
        start_date = start_date,
        tile = tile,
        bbox = bbox,
        end_date = end_date
    )