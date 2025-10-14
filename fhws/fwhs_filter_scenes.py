import os
from json import load
from shapely.geometry import shape

from fhws.fhws_core import geometry_collides_with_bbox


def filter_scenes(collection, data_dir, bbox):
    """
    Return scenes from data_dir where the geometry collides with the bounding box.
    
    Args:
        collection: A string with BDC collection id
        data_dir: A string with directory
        bbox: A tuple in (minx, miny, maxx, maxy) format
        
    Returns:
        list: Scenes filtered by when geometry collides with the bounding box.
    """
    
    # Collection Metadata
    collection_metadata = load(open(os.path.join(data_dir, collection, str(collection+".json")), 'r', encoding='utf-8'))
    
    list_dir = [item for item in os.listdir(os.path.join(data_dir, collection))
            if os.path.isdir(os.path.join(data_dir, collection, item))]
    
    filtered_list = []
    
    for scene in list_dir:
        try:
            item = [item for item in collection_metadata['geoms'] if item["tile"] == scene]
            if (geometry_collides_with_bbox(shape(item[0]['geometry']), bbox)):
                filtered_list.append(item[0]['tile'])   
        except:
            pass
        
    return filtered_list