1. Imputation(Dealing with missing values):
    
    dfa = dfa[dfa.columns[dfa.isna().mean() < threshold]]

    dfa.isna().sum()

    -> Categorical Imputation: 
        dfa["A"] = dfa["A"].fillna(dfa["A"].mode()[0])
        
    -> Numerical Impuation:
        dfa["A"] = dfa["A"].fillna(dfa["A"].mean())
    

    -Check for the duplicate values also, and then remove them
    df.duplicated().value_counts()
    df.drop_duplicates()


2. Handling Outliers: 

    Q1 = dfa["A"].quantile(0.25)
    Q3 = dfa["A"].quantile(0.75)
    IQR = Q3 - Q1
    lower_extreme = Q1-1.5*IQR
    upper_extreme = Q3+1.5*IQR

    outliers = dfa[ (dfa['A'] < lower_extreme) | (dfa['A'] > upper_extreme) ]

    dfa.loc[ dfa['A'] < lower_extreme, "A"] = dfa["A"].mean()
    dfa.loc[ dfa['A'] > upper_extreme, "A"] = dfa["A"].mean()


3. Variable Transformation: 

    dfa["A_B"] = np.log(dfa["A"])
    dfa["A_B"] = (dfa["A"] - dfa["A"].mean())/dfa["A"].std()



4. Categorical Encoding: 

    - one-hot encoding:

    df_one_hot = pd.get_dummies(dfa, columns=['gender', 'education', 'occupation'])
    df_one_hot = df_one_hot.replace({True:1, False:0})

    - label encoding:

    dfa['A'] = dfa['A'].map({'Male':1, 'Female':0})


    - binary encoding.

5. Discretization (Binning): 

    no_of_bins = 3
    bin_labels = ['low', 'medium', 'high']

    dfa["A"] = pd.cut(dfa["A"], bins=no_of_bins, labels=bin_labels)

    dfa["A_B"] = pd.qcut(dfa["A"], q=3, labels=bin_labels)


6. Feature Splitting: 

        Splitting features can involve separating combined or concatenated variables into separate components that may have independent predictive power. For example, splitting a full name into first name and last name.

7. Scaling: 


    dfc = dfa.copy()

    numeric_columns = ['income', 'purchase_amount']

    scaler = StandardScaler()

    dfc[A] = scaler.fit_transform(dfc[A])


8. Feature Creation: 

    bins_no = [18, 25, 35, 50, 65]
    bin_labels = ['18-25', '26-35', '36-50', '51-65']
    dfc["A_B"] = pd.cut(dfc["A"], bins = bins_no, labels = bin_labels)