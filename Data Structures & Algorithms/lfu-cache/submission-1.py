
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}                    # key -> [value, freq]
        self.freq_to_keys = defaultdict(OrderedDict) # freq -> OrderedDict of keys (LRU first)

    def _touch(self, key: int) -> None:
        """Increment the use counter of an existing key."""
        val, freq = self.key_to_val_freq[key]

        # Remove the key from its current frequency bucket
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add it to the next frequency bucket as most recently used
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key][1] = freq + 1

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._touch(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self._touch(key)
            return

        # Evict the LFU key (LRU among ties) if at capacity
        if len(self.key_to_val_freq) >= self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]
            del self.key_to_val_freq[evict_key]

        # Insert the new key with frequency 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1