from dllist import *

class Dictionary(object):
    def __init__(self, num_buckets=250):
        self.map = DoubleLinkedList()
        for i in range(num_buckets):
            self.map.push(DoubleLinkedList())


    def hash_key(self, key):
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key):
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.begin 
            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next
        return bucket, None

    def set(self, key, value):
        bucket, slot = self.get_slot(key)
        if slot:
            slot.value = (key, value)
        else:
            bucket.push((key, value))

    
                
    def get(self, key):
        bucket, node = self.get_slot(key)
        return node and node.value[1] or node

   
        
    def delete(self, key):
        bucket, node = self.get_bucket(key)
        bucket.detach_node(node)

       
    def list(self):
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next    
        
        

            
