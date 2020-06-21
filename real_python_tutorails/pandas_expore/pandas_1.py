
import pandas as pd
import numpy as np


if __name__ == "__main__":

    nba = pd.read_csv("nbaallelo.csv")
    print(type(nba))
    print(len(nba))
    print(nba.shape)


    # display all the columns on the terminal
    pd.set_option("display.max.columns", None)

    # set the precision to 2
    pd.set_option("display.precision",  2)

    print(nba.head())

    print(nba.tail())

    
    #displaying data types
    print(nba.info())

    #displaying basic statistics
    print(nba.describe())

    #to include text data in describe use include

    print(nba.describe(include=np.object))

    #exploring the dataset

    print(nba["team_id"].value_counts())

    print(nba["fran_id"].value_counts())

    """
    It seems that a team named "Lakers" played 6024 games, but only 5078 of those were played by the Los Angeles Lakers. Find out who the other "Lakers" team is:
    """

    print(nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts())


    """
    Indeed, the Minneapolis Lakers ("MNL") played 946 games. You can even find out when they played those games
    """

    print(nba.loc[nba["team_id"] == "MNL", "date_game"].min())
    print(nba.loc[nba["team_id"] == "MNL", "date_game"].max())
    print(nba.loc[nba["team_id"] == "MNL", "date_game"].agg(("min", "max")))



    """
    Pandas datastructure
    """

    #(1) Series

    revenues = pd.Series([5555,  7000, 1980])
    print(revenues)

    """
    revenues.values returns the values in the Series, whereas revenues.index returns the positional index
    """

    
    print(revenues.values)
    print(revenues.index)

    city_revenues = pd.Series(
        [4200, 8000, 6500],
        index=["Amsterdam", "Toronto", "Tokyo"]
    )

    print(city_revenues)

    """
    revenues: This Series behaves like a Python list because it only has a positional index.
city_revenues: This Series acts like a Python dictionary because it features both a positional and a label index.
    """

    city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})
    print(city_employee_count)

    print(city_employee_count.keys())


    #(2) DataFrame

    #makeing dataFrame from Series

    city_data = pd.DataFrame({
        "revenue": city_revenues,
        "employee_count": city_employee_count
    })

    print(city_data)

    print(city_data.index)

    print(city_data.values)

    print(city_data.axes)

    #axes o corresponds to row and 1 corresponds to column
    print(city_data.axes[0])

    print(nba.index)

    print(nba.axes)

    print(nba.keys())

    print(nba.axes[0])


    """
    Accessing series elemens
    """

    #(1)
    #using the indexing operator
    """
    A positional or implicit index, which is always a RangeIndex
    A label or explicit index, which can contain any hashable objects
    """

    print(city_revenues)

    #Series can be accessed as a list
    print(city_revenues["Tokyo"])
    print(city_revenues[2])
    print(city_revenues[-1])
    print(city_revenues["Toronto":])


    #using .loc, .iloc

    colors = pd.Series(
        ["red", "purple", "blue", "green", "yellow"],
        index=[1, 2, 3, 5, 8]
    )

    print(colors)

    """
    What will colors[1] return? For a positional index, colors[1] is "purple". However, if you go by the label index, then colors[1] is referring to "red"
    """
    print(colors.loc[1])  # refers to label index
    print(colors.iloc[1]) # refers to positional index

    """
    .loc and .iloc also support the features you would expect from indexing operators, like slicing. However, these data access methods have an important difference. While .iloc excludes the closing element, .loc includes it
    """
    print(colors.iloc[1:3])
    print(colors.loc[1:3])
    print(colors.iloc[-2])

    """
    You can use .iloc on a Series similar to using [] on a list.
    You can use .loc on a Series similar to using [] on a dictionary.
    """

    """
    Accessing DataFrame Elements
    """

    print(city_data["revenue"])
    print(city_data.revenue)
    print(type(city_data["revenue"]))

    """
    The indexing operation toys["shape"] returns the correct data, but the attribute-style operation toys.shape still returns the shape of the DataFrame. You should only use attribute-style accessing in interactive sessions or for read operations
    """
    toys = pd.DataFrame([
        {"name": "ball", "shape": "sphere"},
        {"name": "Rubik's cube", "shape": "cube"}
    ])
    print(toys)
    print(toys["shape"])
    print(toys.shape)    #dont use it for dataFrame



    #using .loc and .iloc

    print(city_data)

    print(city_data.loc["Amsterdam"]) #selects the row with the label index "Amsterdam".

    print(city_data.loc["Tokyo": "Toronto"]) #selects the rows with label indices from "Tokyo" to "Toronto". Remember, .loc is inclusive

    print(city_data.iloc[1]) #selects the row with the positional index 1, which is "Tokyo".


    print(nba.iloc[-2])

    print(city_data.loc["Amsterdam": "Tokyo", "revenue"])  #first param is row and second param is column

    print(nba.loc[5555:5559, ["fran_id", "opp_fran", "pts", "opp_pts"]])

    #Querying Your Dataset

    current_decade = nba[nba["year_id"] > 2010]
    print(current_decade)


    games_with_notes = nba[nba["notes"].notnull()]
    print(games_with_notes)

    ers = nba[nba["fran_id"].str.endswith("ers")]
    print(ers)

    joint_criteria = nba[
        (nba["_iscopy"] == 0) &
        (nba["pts"] > 100) &
        (nba["opp_pts"] > 100) &
        (nba["team_id"] == "BLB")
    ]   #Here, you use nba["_iscopy"] == 0 to include only the entries that arent copies

    print(joint_criteria)



    #Grouping and Aggregating Your Data
    print(city_revenues)

    print(city_revenues.sum())

    print(city_revenues.max())

    #since columns are seires

    print(nba["pts"].sum())


    print(nba.groupby("fran_id", sort=False)["pts"].sum())

    print(nba[
    (nba["fran_id"] == "Spurs") &
    (nba["year_id"] > 2010)
].groupby(["year_id", "game_result"])["game_id"].count())

    print(nba[(nba["fran_id"] == "Warriors") & (nba["year_id"] == 2015)].groupby(["is_playoffs", "game_result"])["game_id"].count())


    #Manipulating Columns

    #copy
    df = nba.copy()

    #new columns
    df["difference"] = df.pts - df.opp_pts


    #renaming columns

    renamed_df = df.rename( columns={"game_result": "result", "game_location": "location"})

    print(renamed_df.info())

    """
    Like several other data manipulation methods, .rename() returns a new DataFrame by default. If you want to manipulate the original DataFrame directly, then .rename() also provides an inplace parameter that you can set to True.
    """

    #droping columns

    print(df.shape)

    elo_columns = ["elo_i", "elo_n", "opp_elo_i", "opp_elo_n"]
    df.drop(elo_columns, inplace=True, axis=1)

    print(df.shape)



    #specify the datatypes

    df["date_game"] = pd.to_datetime(df["date_game"])

    df["game_location"].nunique()

    df["game_location"].value_counts()

    """
    categorical data has a few advantages over unstructured text. When you specify the categorical data type, you make validation easier and save a ton of memory, as Pandas will only use the unique values internally. The higher the ratio of total values to unique values, the more space savings youll get
    """
    df["game_location"] = pd.Categorical(df["game_location"])
    df["game_location"].dtype




    #cleaning data

    rows_without_missing_data = nba.dropna()

    print(rows_without_missing_data.shape)


    data_without_missing_columns = nba.dropna(axis=1)
    print(data_without_missing_columns.shape)

    #If theres a meaningful default value for your use case, then you can also replace the missing values with that
    data_with_default_notes = nba.copy()
    data_with_default_notes["notes"].fillna(
        value="no notes at all",
        inplace=True
    )
    data_with_default_notes["notes"].describe()



    #Combining Multiple Datasets

    print(city_data)

    further_city_data = pd.DataFrame(
        {"revenue": [7000, 3400], "employee_count":[2, 2]},
        index=["New York", "Barcelona"]
    )

    print(further_city_data)

    #You can add these cities to city_data using .concat():

    all_city_data = pd.concat([city_data, further_city_data], sort=False)

    print(all_city_data)

    """
    By default, concat() combines along axis=0. In other words, it appends rows. You can also use it to append columns by supplying the parameter axis=1:
    """

    city_countries = pd.DataFrame({
        "country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
        "capital": [1, 1, 0, 0, 0]},
                                  index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"]
    )
    cities = pd.concat([all_city_data, city_countries], axis=1, sort=False)
    print(cities)

    """
    if you want to combine only the cities that appear in both DataFrame objects, then you can set the join parameter to inner
    """
    pd.concat([all_city_data, city_countries], axis=1, join="inner")


    countries = pd.DataFrame({
        "population_millions": [17, 127, 37],
        "continent": ["Europe", "Asia", "North America"]
    }, index= ["Holland", "Japan", "Canada"])
    new_countries = pd.merge(cities, countries, left_on="country", right_index=True)

    print(new_countries)

    # to include those without country data:

    new_countries = pd.merge(cities, countries, left_on="country", right_index=True, how="left")

    print(new_countries)
            
    
    

    

    



    
    
    
    
    




    
