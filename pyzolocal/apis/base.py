from typing import Callable, Dict


def get_sql_api_map() -> Dict[str, Callable]:
    from ..sqls import gets

    return {k: v for k, v in gets.__dict__.items() if k.startswith("get_")}


def get_prefs_api_map() -> Dict[str, Callable]:
    from ..prefs import gets

    return {k: gets.__dict__[k] for k in gets.__all__}


def get_files_api_map() -> Dict[str, Callable]:
    from ..files import gets

    return {k: gets.__dict__[k] for k in gets.__all__}
