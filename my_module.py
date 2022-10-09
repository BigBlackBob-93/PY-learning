def del_file(name):
    import os
    if os.path.isfile(name):
        os.remove(name)
        return True
    else:
        return False


actor = 'Edward Norton'

