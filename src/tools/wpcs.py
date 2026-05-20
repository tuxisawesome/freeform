import catalogLib

def die(err):
    print(err)

def main():
    loadedCatalog = None
    while True:
        if loadedCatalog == None:
            x = input(f"WPCS (none) > ")
        else:
            x = input(f"WPCS ({loadedCatalog.catalogName}) > ")
        if x.lower().startswith("create"):
            filename = x.split(" ")[1]
            catalogName = input("Name? ")
            catalogDesc = input("Description? ")
            ret = catalogLib.create_catalog(catalogName, catalogDesc, filename)
            if ret != True:
                die("Catalog Creation Error: " + ret)
        elif x.lower() == "help":
            print("Walter's Paper Cataloging System")
            print("Readmodes: 1 (By name), 2 (By Id), 3 (By Desc.)")
            print("======================== Commands:")
            print("create           [catalogFileName]")
            print("write")
            print("======================== Operations")
            print("load             [catalogFileName]")
            print("get              [input] [readmode]")
            print("get.all")
            print("remove           [input] [readmode]")
            print("remove.all")
            print("add")
            print("======================== Metadata Editor")
            print("meta.name[.edit]")
            print("meta.desc[.edit]")
            print("======================== Other")
            print("exit")
        elif x.lower() == "write":
            x = catalogLib.write_catalog(loadedCatalog)
            if x != True:
                die("Catalog write error: " + x)
        elif x.lower().startswith("load"):
            if len(x.split()) > 2:
                print("Too many arguments... Maybe you meant 'get'?")
                continue
            loadedCatalog = catalogLib.read_catalog(x.split()[1])
            print(f"Loaded catalog: {loadedCatalog.catalogName}")
        elif x.lower() == "exit":
            print("Bye!")
            return
        elif x.lower() == "get.all":
            for i in range(len(loadedCatalog.Documents.documentIds)):
                print(f"{loadedCatalog.Documents.documentIds[i-1]} === {loadedCatalog.Documents.documentNames[i-1]} ::: {loadedCatalog.Documents.documentDesc[i-1]}")
        elif x.lower().startswith("get"):
            name, desc, id = catalogLib.get_entry(loadedCatalog, x.split()[1], int(x.split()[2]))
            print(f"{id} === {name} ::: {desc}")
        elif x.lower() == "remove.all":
            loadedCatalog.Documents.documentDesc.clear()
            loadedCatalog.Documents.documentNames.clear()
            loadedCatalog.Documents.documentIds.clear()
            print("All clear")
        elif x.lower().startswith("remove"):
            loadedCatalog = catalogLib.remove_entry(loadedCatalog, x.split()[1], int(x.split()[2]))
        elif x.lower() == "add":
            name = input("Name? ")
            desc = input("Desc? ")
            id = input("Id (blank for seq.)? ")
            if id == "":
                loadedCatalog = catalogLib.add_entry(loadedCatalog, name, desc, None)
            else:
                loadedCatalog = catalogLib.add_entry(loadedCatalog, name, desc, id)
        elif x.lower() == "meta.name.edit":
            newName = input("Name? ")
            loadedCatalog = catalogLib.change_name(loadedCatalog, newName)
            print("Name changed")
        elif x.lower() == "meta.desc.edit":
            newName = input("Desc? ")
            loadedCatalog = catalogLib.change_name(loadedCatalog, newName)
            print("Description changed")
        elif x.lower() == "meta.name": print(f"Name: {loadedCatalog.catalogName}")
        elif x.lower() == "meta.desc": print(f"Description: {loadedCatalog.catalogDesc}")
        elif x == "": continue
        else:
            print("Invalid command. Try 'help'.")

main()