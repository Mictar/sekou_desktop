import pandas as pd

def convert(classe):
    file_name = f"/home/moctar/Bureau/sekou_cisse/sekou_desktop/desktop/desktop/core/data/eleves/listes/liste {classe} année.ods"
    
    data =  pd.read_excel(file_name, engine="odf")

    write = pd.DataFrame()
    write["N° ordre"] = [ str(i + 1) for i in range(len(data["Noms"]))]
    write["Prenoms"] = data["Prenoms"]
    write["Noms"] = data["Noms"]
    
    #print(write.keys())
    print(f"[*] process {file_name}")
    outfile = f"/home/moctar/Bureau/sekou_cisse/sekou_desktop/desktop/desktop/core/data/notes/listes/liste {classe} année.ods"
    #outfile = f"~/Bureau/listes/liste {classe} année.xlsx"

    write.to_excel(outfile, index=False, engine="odf")


def main():
    for i in range(1, 10):
    
        convert(i)

main()
