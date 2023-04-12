import numpy as np
# Pembuatan kolom bill terakhir
def total_pay(df):
    df['total_pay'] = (df['pay_amt_1']+df['pay_amt_2']+df['pay_amt_3']+df['pay_amt_4']+df['pay_amt_5']+df['pay_amt_6'])
    return df

# pembuatan kolom jumlah dari pay
def last_bill(df):
    df['last_bill'] = df['bill_amt_1']
    return df

# # Pembuatan ratio pembayaran antara tagihan dan pembayaran
def pay_ratio(df):
    df['pay_ratio'] = (df['total_pay']-df['last_bill'])/df['limit_balance']
    return df


# # pengkategorian limit_balance
def add_credit_limit_category(df, balance_col):
    # copy the dataframe to avoid modifying the original
    dataset = np.array(df[balance_col])

    # create a new column based on the conditions
    conditions = [
        dataset <= 50000,
        np.logical_and(dataset > 50000, dataset <= 140000),
        np.logical_and(dataset > 140000, dataset <= 230000),
        dataset > 230000
    ]
    choices = [0, 1, 2, 3] # 0= low limit, 1= mid limit, 2= high limit, 3= very high limit
    df['credit_limit_category'] = np.select(conditions, choices)
    
    return df