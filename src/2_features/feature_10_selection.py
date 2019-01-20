#%%
# The final selection of columns from the main DF
cols_to_use = ['Type', 'Age', 'Breed1', 'Breed2', 'Gender', 'Color1', 'Color2', 'Color3', 'MaturitySize', 'FurLength',
               'Vaccinated', 'Dewormed', 'Sterilized', 'Health', 'Quantity', 'Fee', 'State', 'RescuerID', 'VideoAmt',
               'PhotoAmt', 'AdoptionSpeed', 'No_name', 'Pure_breed', 'health', 'Free',
               'score', 'magnitude']

cols_to_discard = [
    'RescuerID',
    'Description',
    'Name',
]


logging.debug("Feature selection".format())
original_columns = df_all.columns
# col_selection = [col for col in all_columns if col not in cols_to_discard]

df_all.drop(cols_to_discard,inplace=True, axis=1)

logging.debug("Selected {} of {} columns".format(len(df_all.columns),(original_columns)))
logging.debug("Size of df_all with selected features: {} MB".format(sys.getsizeof(df_all)/1000/1000))

logging.debug("Record selection (sampling)".format())
logging.debug("{} fraction sampling".format(SAMPLE_FRACTION))
df_all = df_all.sample(frac=SAMPLE_FRACTION)
logging.debug("Final size of data frame: {}".format(df_all.shape))
logging.debug("Size of df_all with selected features and records: {} MB".format(sys.getsizeof(df_all)/1000/1000))
