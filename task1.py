import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt


def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return list(df)

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df['type'].unique()

def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]

def exercise_7(df):
    df1 = df.groupby('nameOrig')['nameDest'].agg(['nunique'])
    df1.sort_values(by=('nunique'), ascending=False, inplace=True)
    return df1

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()
    def transaction_counts_split_by_fraud(df):
        return df.groupby(by=['type', 'isFraud']).size()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types Frequencies')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Occurrence')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types Frequencies, Split by Fraud')
    axs[1].set_xlabel('Transaction Type, (where Fraud exists: ("type", 1))')
    axs[1].set_ylabel('Occurrence')
    fig.suptitle('Transaction Types')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'The data suggests that fraudelent activity is only seen in "CASH_OUT" and "TRANSFER" transactions. As such, it is recommended that management should focus on improving the security and reviewing on transactions in these two sectors.'

visual_1(df)

def visual_2(df):
    def query(df):
        df['Origin Delta'] = df['oldbalanceOrg'] -df['newbalanceOrig']
        df['Destination Delta'] = df['oldbalanceDest'] -df['newbalanceDest']
        return df[df['type']=='CASH_OUT']
    plot = query(df).plot.scatter(x='Origin Delta',y='Destination Delta')
    plot.set_title('Source v. Destination Balance Delta for Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return '"CASH_OUT" refers to the withdrawal of physical money. Only half of the quadrants have any activity, indicating that the dataset is sound. The y = -x line where x >= 0 suggests an instant settlement.'

visual_2(df)

fraud_count = df[df['isFraud'] == 1].value_counts()
flagged_count = df[df['isFlaggedFraud'] == 1].value_counts()

def exercise_custom(df1, df2):
    df = pd.DataFrame([True] * len(df1) + [False] * len(df2))
    return(df)

def visual_custom():
    g_q1 = sns.catplot(x=0, kind='count', order=[True, False], data=exercise_custom(fraud_count, flagged_count), height=4, aspect=1)
    g_q1.set(xlabel='Flagged or Frauded?', ylabel='Number of Instances')
    g_q1.set_xticklabels(labels=['Fraud', 'Flagged'])
    
    plt.tight_layout()
    plt.title('How much of the Data was flagged or frauded?')
    plt.show()
