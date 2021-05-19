import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['Tree Species'].tolist())

    TreeSpecies_data    = df['Tree Species'].tolist()

    PercentageInOntario_data = df['Percentage in Ontario'].tolist()

    # print(df['quebec'].tolist())

    result_dict = {
       
        'Tree Species'    : TreeSpecies_data,
        'Percentage in Ontario' : PercentageInOntario_data
    }

    # print(result_dict)

    return result_dict

def add_row(TreeSpecies, PercentageInOntario):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        
        'Tree Species'    : TreeSpecies, 
        'Percentage in Ontario' : PercentageInOntario
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()
