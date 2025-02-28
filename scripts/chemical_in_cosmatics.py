def condition(name, df):
    '''
    this function takes the top 5 chemicals and return all other 
    chemical names as 'others' to make it easier to plot 
    '''
    top_5 = df.ChemicalName.head(5).to_list()
    if name in top_5:
        return name
    else:
        return 'others'
    

def others(df):
    '''
    this function takes a data frame and check all chemical names in it 
    using condition() function and return a new column with the new names

    '''
    new_col = df.ChemicalName.apply(lambda name: condition(name, df))
    return new_col