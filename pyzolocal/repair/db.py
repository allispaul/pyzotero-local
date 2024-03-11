import os

from ..prefs.common import KEY_STORAGE, dataDir
from ..sqls import gets


def insert_disappear_dir_in_db():
    """"""
    storage_root = os.path.join(dataDir(), KEY_STORAGE)
    storage_dirs = set(os.listdir(storage_root))
    db_keys = [attach.key for attach in gets.get_attachments()]

    sql = """
        INSERT INTO items (itemTypeID, libraryID, key)
            VALUES ({}, {}, {});
        """  # noqa: F841
    # TODO execte sql
    res = []
    for key in storage_dirs:
        if not os.path.isdir(os.path.join(storage_root, key)):
            continue
        if key not in db_keys:
            res.append(os.path.join(storage_root, key))
