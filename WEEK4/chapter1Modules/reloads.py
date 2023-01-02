import importlib
import chapter1Modules.sample as sample

importlib.reload(sample)
importlib.reload(sample)
importlib.reload(sample)


import chapter1Modules.filechanges as filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass
    
for i in range(5):
    changes()
    input('Hit enter to reload...')



