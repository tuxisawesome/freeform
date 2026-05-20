
debug = True

class Catalog:
    catalogName = ""
    catalogDesc = ""
    fileName = ""
    class Documents:
        documentNames = []
        documentIds = []
        documentDesc = []


def create_catalog(catalogName,catalogDesc,fileName):
    with open(fileName + ".wpcs", "w") as ctlg:
        ctlg.writelines([f"# WPCS Standardized Catalog System\n", f"${catalogName}```{catalogDesc}\n"])
        ctlg.close()
    return True

def read_catalog(fileName):
    catalog = Catalog
    catalog.fileName = fileName
    with open(f"{fileName}.wpcs", "r") as ctlg:
        for line in ctlg.readlines():
            if line.startswith("#") or line == "":
                continue
            elif line.startswith("$"):
                x = line.strip("\n").split("```")
                catalog.catalogName = x[0][1:]
                catalog.catalogDesc = x[1]
            elif line.startswith("%"):
                # Catalog Entry
                x = line.strip("\n").split("```")
                catalog.Documents.documentIds.append(x[0][1:])
                catalog.Documents.documentNames.append(x[1])
                catalog.Documents.documentDesc.append(x[2])
                if debug:
                    print(f"*   Added {x[1]} to catalog")
        ctlg.close()
    return catalog


def write_catalog(catalog : Catalog, filename=None):
    if filename == None: fn = catalog.fileName
    else: fn = filename

    if debug: print(f"Writing to {fn}")
    with open(f"{fn}.wpcs", "w") as ctlg:
        ctlg.writelines([f"# WPCS Standardized Catalog System\n", f"${catalog.catalogName}```{catalog.catalogDesc}\n"])
        for docid in catalog.Documents.documentIds:
            ctlg.write(f"%{docid}```{catalog.Documents.documentNames[catalog.Documents.documentIds.index(docid)]}```{catalog.Documents.documentDesc[catalog.Documents.documentIds.index(docid)]}\n")
            if debug: print(f"*   Wrote {docid} to catalog")
        ctlg.close()
    return True

def add_entry(catalog : Catalog, name, desc, id=None):
    nc = catalog
    if id == None:
        if len(nc.Documents.documentIds) == 0:
            newId = "1"
        else:
            newId = str(int(nc.Documents.documentIds[-1]) + 1)
    else:
        newId = id
    nc.Documents.documentIds.append(newId)
    nc.Documents.documentNames.append(name)
    nc.Documents.documentDesc.append(desc)
    return nc

# read mode 1: Names
# read mode 2: Id
# read mode 3: Desc
def remove_entry(catalog : Catalog, input, read_mode : int):
    nc = catalog
    if read_mode == 2:
        targetid = int(input)
    if read_mode == 1:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentNames.index(input)])
    if read_mode == 3:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentDesc.index(input)])
    targetId = targetid    
    # Delete the entry
    nc.Documents.documentDesc.pop(nc.Documents.documentIds.index(str(targetId)))
    nc.Documents.documentNames.pop(nc.Documents.documentIds.index(str(targetId)))
    nc.Documents.documentIds.pop(nc.Documents.documentIds.index(str(targetId)))
    return nc

def get_entry(catalog : Catalog, input, read_mode : int):
    nc = catalog
    if read_mode == 2:
        targetid = int(input)
    if read_mode == 1:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentNames.index(input)])
    if read_mode == 3:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentDesc.index(input)])
    targetId = targetid    
    # Delete the entry
    desc = nc.Documents.documentDesc[nc.Documents.documentIds.index(str(targetId))]
    name = nc.Documents.documentNames[nc.Documents.documentIds.index(str(targetId))]
    id = nc.Documents.documentIds[nc.Documents.documentIds.index(str(targetId))]
    return name, desc, id

def change_name(catalog : Catalog, newName):
    nc = catalog
    nc.catalogName = newName
    return nc

def change_desc(catalog : Catalog, newDesc):
    nc = catalog
    nc.catalogDesc = newDesc
    return nc