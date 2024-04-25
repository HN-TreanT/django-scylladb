from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from .config import *
class QdrantTest:
    def __init__(self):
        self.client = QdrantClient(VDPIP, port=VDBPORT)
    def create_collection(self, collection_name):
        vectors_config = VectorParams(size=4,  distance=Distance.DOT)
        self.client.create_collection(collection_name=collection_name, vectors_config=vectors_config)    
        return True
    def add_vector(self, collection_name, points):
        self.client.upsert(collection_name, wait=True, points=points)
        return True