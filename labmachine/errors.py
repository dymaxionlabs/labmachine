class BlobNotFound(Exception):
    def __init__(self, bucket, key):
        msg = f"Key {key} not found in bucket {bucket}"
        super().__init__(msg)


class BucketNotFound(Exception):
    def __init__(self, bucket):
        msg = f"{Bucket} not found"
        super().__init__(msg)


class BucketForbidden(Exception):
    def __init__(self, bucket):
        msg = f"Not permissions for {bucket}"
        super().__init__(msg)
