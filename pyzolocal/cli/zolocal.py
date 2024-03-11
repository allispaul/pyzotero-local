from fire import Fire

from pyzolocal import __version__
from pyzolocal.prefs.base import is_linux, is_mac, is_win, profile_root
from pyzolocal.prefs.common import dataDir


def main(*args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        version_display = f"""pyzolocal version {__version__}
        |Win: {is_win()}|MAC: {is_mac()}|Linue: {is_linux()}|
        zotero.profile_directory = {profile_root()}
        zotero.dataDir = {dataDir()}
        """
        print(version_display)


Fire(main)
exit(0)
