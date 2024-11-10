import pandas as pd

def excelRender(table):

    df = pd.DataFrame(table)

    # Export the DataFrame to an Excel file
    df.to_excel('output.xlsx', index=False)
        