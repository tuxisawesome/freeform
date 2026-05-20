debug = True

class Documents:
    def __init__(self):
        # Using self. guarantees unique lists for every instance
        self.documentNames = []
        self.documentDesc = []
        self.documentIds = []

class Catalog:
    def __init__(self):
        self.catalogName = ""
        self.catalogDesc = ""
        self.fileName = ""
        # Nesting the Documents object
        self.Documents = Documents()


def create_catalog(catalogName, catalogDesc, fileName):
    with open(fileName + ".wpcs", "w") as ctlg:
        ctlg.writelines([
            "# WPCS Standardized Catalog System\n",
            f"${catalogName}```{catalogDesc}\n"
        ])
    return True


def read_catalog(fileName):
    catalog = Catalog()  # FIX: call the class to create a fresh instance
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
    return catalog


def write_catalog(catalog: Catalog, filename=None):
    if filename is None:
        fn = catalog.fileName
    else:
        fn = filename

    if debug:
        print(f"Writing to {fn}")
    with open(f"{fn}.wpcs", "w") as ctlg:
        ctlg.writelines([
            "# WPCS Standardized Catalog System\n",
            f"${catalog.catalogName}```{catalog.catalogDesc}\n"
        ])
        for docid in catalog.Documents.documentIds:
            idx = catalog.Documents.documentIds.index(docid)
            ctlg.write(
                f"%{docid}```{catalog.Documents.documentNames[idx]}"
                f"```{catalog.Documents.documentDesc[idx]}\n"
            )
            if debug:
                print(f"*   Wrote {docid} to catalog")
    return True


def add_entry(catalog: Catalog, name, desc, id=None):
    nc = catalog
    if id is None:
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
def remove_entry(catalog: Catalog, input, read_mode: int):
    nc = catalog
    if read_mode == 2:
        targetid = int(input)
    if read_mode == 1:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentNames.index(input)])
    if read_mode == 3:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentDesc.index(input)])
    targetId = targetid
    # Delete the entry
    idx = nc.Documents.documentIds.index(str(targetId))
    nc.Documents.documentDesc.pop(idx)
    nc.Documents.documentNames.pop(idx)
    nc.Documents.documentIds.pop(idx)
    return nc


def get_entry(catalog: Catalog, input, read_mode: int):
    nc = catalog
    if read_mode == 2:
        targetid = int(input)
    if read_mode == 1:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentNames.index(input)])
    if read_mode == 3:
        targetid = int(nc.Documents.documentIds[nc.Documents.documentDesc.index(input)])
    targetId = targetid
    # Retrieve the entry
    idx = nc.Documents.documentIds.index(str(targetId))
    desc = nc.Documents.documentDesc[idx]
    name = nc.Documents.documentNames[idx]
    id = nc.Documents.documentIds[idx]
    return name, desc, id


def change_name(catalog: Catalog, newName):
    nc = catalog
    nc.catalogName = newName
    return nc


def change_desc(catalog: Catalog, newDesc):
    nc = catalog
    nc.catalogDesc = newDesc
    return nc