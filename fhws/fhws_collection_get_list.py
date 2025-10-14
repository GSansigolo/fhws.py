from tqdm import tqdm

def collection_get_list(stac, datacube):

    collection = datacube['collection']
    bbox = datacube['bbox']
    start_date = datacube['start_date']
    end_date = datacube['end_date']
    bands = datacube['bands'] 

    if (datacube['bbox']):
        item_search = stac.search(
            collections=[collection],
            datetime=start_date+"T00:00:00Z/"+end_date+"T23:59:00Z",
            bbox=bbox,
            limit=365
        )
        
    band_dict = {}
    for band in bands:
        band_dict[band] = []

    for item in tqdm(desc='Fetching... ', unit=" scenes", total=item_search.matched(), iterable=item_search.items()):
        for band in bands:
            asset = item.assets.get(band)
            if asset and hasattr(asset, 'href'):
                band_dict[band].append(asset.href)

    return band_dict