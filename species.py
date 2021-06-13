import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    # print(df['Tree Species'].tolist())

    TreeSpecies_data           = df['Tree Species'].tolist()

    PercentageInOntario_data   = df['Percentage in Ontario'].tolist()

    # print(df['quebec'].tolist())

    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    result_dict = {
        'Tree Species'                  : TreeSpecies_data,
        'Percentage in Ontario'         : PercentageInOntario_data,
        'data_list'                     : list_of_tuples
    }

    

    # print(result_dict)

    return result_dict

if __name__ == "__main__":
    get_data()
