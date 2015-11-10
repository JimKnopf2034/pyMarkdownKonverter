import locale
import os

folders = {
    'de_DE': '~/Vorlagen',
    'en_US':'~/Templates'
}


def getDefaultTemplateDir():
    local = locale.getdefaultlocale()
    return os.path.expanduser(folders[local[0]])
