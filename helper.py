def fetch_medal_tally(df, year, country):
    if year == 'Overall' and country == 'Overall':
        temp_df = df
    elif year == 'Overall' and country != 'Overall':
        temp_df = df[df['Region'] == country]
    elif year != 'Overall' and country == 'Overall':
        temp_df = df[df['Year'] == int(year)]
    else:
        temp_df = df[(df['Year'] == int(year)) & (df['Region'] == country)]

    medal_tally = temp_df[temp_df['Medal'] != 'No Medal']
    medal_tally = medal_tally.groupby('Region')[['Medal']].value_counts().unstack(fill_value=0)

    medal_tally['Total'] = medal_tally.sum(axis=1)
    medal_tally = medal_tally.sort_values('Total', ascending=False).reset_index()

    return medal_tally


def country_list(df):
    countries = df['Region'].dropna().unique().tolist()
    countries.sort()
    countries.insert(0, 'Overall')
    return countries


def year_list(df):
    years = df['Year'].dropna().unique().tolist()
    years = sorted(list(map(int, years)))
    years.insert(0, 'Overall')
    return years