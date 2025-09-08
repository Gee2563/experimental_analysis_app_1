import pandas as pd
from scipy import stats

def stats_calculator(provided_data, variables):
    """
    Function to calculate basic statistics for given variables in a DataFrame.
    Args:
        provided_data (pd.DataFrame): DataFrame containing the data.
        columns (list): List of column names to calculate statistics for.
        variables (list): List of variable names corresponding to the columns.
        stats_df_cols (list): List of statistic names to be used as columns in the output DataFrame.
    
    """
    stats_df = pd.DataFrame(columns=['variable','mean','std. dev.','max','min'])
    stats_df['variable'] = variables
    for var in variables:
        col = provided_data[var].dropna()
        stats_df.loc[stats_df['variable']==var, 'mean']    = round(col.mean(), 2)
        stats_df.loc[stats_df['variable']==var, 'std. dev.'] = round(col.std(),  2)
        stats_df.loc[stats_df['variable']==var, 'max']     = round(col.max(),  2)
        stats_df.loc[stats_df['variable']==var, 'min']     = round(col.min(),  2)

    stats_df.set_index('variable', inplace=True)
    return stats_df


def objective_randomization(provided_data, variables):
    """
    
    Function to perform t-tests for given variables between two treatment groups in a DataFrame.
    Args:
        provided_data (pd.DataFrame): DataFrame containing the data.
        variables (list): List of variable names to perform t-tests on.
    
    Returns:
        pd.DataFrame: DataFrame containing t-statistics and p-values for each variable.

    
    """

    ttest_df = pd.DataFrame(columns=['variable','t-statistic','p-value'])
    ttest_df['variable'] = variables
    
    g1 = provided_data[provided_data['treatment']=='k1_8_lot_exp']
    g2 = provided_data[provided_data['treatment']=='k1_8_exp_lot']

    for var in ttest_df['variable']:
        arr1 = g1[var].dropna()
        arr2 = g2[var].dropna()
        t_stat, p_val = stats.ttest_ind(arr1, arr2, equal_var=False)
        ttest_df.loc[ttest_df['variable']==var, 't-statistic'] = round(t_stat, 2)
        ttest_df.loc[ttest_df['variable']==var, 'p-value']     = round(p_val, 2)

    ttest_df.set_index('variable', inplace=True)
    return ttest_df
