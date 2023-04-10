import pandas as pd

def dataClean(df1, df2):
    df = combineData(df1, df2) #does a left join for the two data

    #fills in the missing publisher values    
    df.loc[df['Name'].isin(['3-D Man', 'Agent  13', 'Blizzard I', 'Boom Boom', 'Chuck Norris', 'Crimson Dynamo I', 'Goliath II', 'Goliath III', 'Ironman', 'Jack Bauer',
                                    'Kool-Aid Man', 'Ms Marvel', 'Mysterio I', 'Spiderman','Sub-Mariner', 'Vindicator II', 'Willis Stryker']), 'Publisher'] = 'Marvel Comics'
    df.loc[df['Name'].isin(['Astro Boy']), 'Publisher'] = 'Kobunsha'
    df.loc[df['Name'].isin(['Atom I', 'Batgirl I', 'Batgirl II','Black Canary I','Black Canary II','Blue Beetle I','Cheetah I',
                                        'Flash Gordon','Flash I','Hawkwoman I','Oracle (DC)','Robin I','Silk Spectre I']), 'Publisher'] = 'DC Comics'
    df.loc[df['Name'].isin(['Darkside', 'The Cape']), 'Publisher'] = 'IDW Publishing'
    df.loc[df['Name'].isin(['Jack-jack', 'Violet']), 'Publisher'] = 'Dark Horse Comics'
    df.loc[df['Name'].isin(['Super Moos']), 'Publisher'] = 'Crystal Mosaic Books'

    #sets all stats over 100 to 100
    df.loc[(df['Intelligence'] > 100), 'Intelligence'] = 100
    df.loc[(df['Strength'] > 100), 'Strength'] = 100
    df.loc[(df['Speed'] > 100), 'Speed'] = 100
    df.loc[(df['Durability'] > 100), 'Durability'] = 100
    df.loc[(df['Power'] > 100), 'Power'] = 100
    return df


def combineData(df1, df2):
    #takes only Name and Publisher as columns then joins the two tables together
    df2 = df2[['Name', 'Publisher']]
    df = df1.join(df2.set_index('Name'), on='Name')
    df_unique = df.drop_duplicates(keep=False)
    return df_unique




# df_unique.loc[df_unique['Name'].isin(['3-D Man']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Agent 13']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Astro Boy']), 'Publisher'] = 'Kobunsha'
# df_unique.loc[df_unique['Name'].isin(['Atom I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Batgirl I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Batgirl II']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Black Canary I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Black Canary II']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Blizzard I']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Blue Beetle I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Boom Boom']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Cheetah I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Chuck Norris']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Crimson Dynamo I']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Darkside']), 'Publisher'] = 'IDW Publishing'
# df_unique.loc[df_unique['Name'].isin(['Flash Gordon']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Flash I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Goliath II']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Goliath III']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Hawkwoman I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Ironman']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Jack Bauer']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Jack-jack']), 'Publisher'] = 'Dark Horse Comics'
# df_unique.loc[df_unique['Name'].isin(['Kool-Aid Man']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Ms Marvel']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Mysterio I']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Oracle (DC)']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Robin I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Silk Spectre I']), 'Publisher'] = 'DC Comics'
# df_unique.loc[df_unique['Name'].isin(['Spiderman']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Sub-Mariner']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Super Moos']), 'Publisher'] = 'Crystal Mosaic Books'
# df_unique.loc[df_unique['Name'].isin(['The Cape']), 'Publisher'] = 'IDW Publishing'
# df_unique.loc[df_unique['Name'].isin(['Vindicator II']), 'Publisher'] = 'Marvel Comics'
# df_unique.loc[df_unique['Name'].isin(['Violet']), 'Publisher'] = 'Dark Horse Comics'
# df_unique.loc[df_unique['Name'].isin(['Willis Stryker']), 'Publisher'] = 'Marvel Comics'