Apologies for the oversight. Handling outliers is an important step in feature engineering as well. Here is the revised order, including handling outliers:

1. Imputation(Dealing with missing values):

        delete record / fill with mean

        -> Categorical Imputation:  missing cat. values replaced with mostly occuring values
        -> Numerical Impuation:     missing num. values are replaced with mean.

2. Handling Outliers: 

        Identify and handle outliers in the data. Outliers can be treated by removing them, transforming them, or replacing them with more representative values.

3. Variable Transformation: 

        Apply transformations to variables as needed. This can include logarithmic, exponential, or Box-Cox transformations to handle skewed distributions or create new features that capture interactions or patterns in the data.

        log transformation is applied to those attributes where is skewed distribution, majority values in narrow range.


4. Categorical Encoding: 

        Convert categorical variables into numerical representations 
            that can be understood by machine learning algorithms. This can be done using techniques like 
            - one-hot encoding, 
            - label encoding, 
            - binary encoding.

5. Discretization (Binning): 

        It involves essentially taking a set of values of data and grouping sets of them 
        together in some logical fashion into bins (or buckets).
        Binning can be applied to numerical value and categorical value

        The grouping data is as follows:
        1. Group based on equal intervals
        2. Grouping based on equal frequencies
        3. Grouping based on decision tree sorting(to establish relation with target)


6. Feature Splitting: 

        Splitting features can involve separating combined or concatenated variables into separate components that may have independent predictive power. For example, splitting a full name into first name and last name.

7. Scaling: 

        Scale numerical variables to a similar range. Common scaling techniques include standardization (subtracting the mean and dividing by the standard deviation) or normalization (scaling values between 0 and 1).

        Transforming the values in a dataset to a specific range or distribution
     -) Scalling is needed when variables have different units, it can affect the performance
        of certain algorithms and statistical analysis.
     -) It is a common step to ensure that variables are comparible and don't ensure the bias
        ans distortion in the analysis.
    TYPES:
        1) Min-max scalling:
            This process involves the rescaling of all values in a feature in the range 0 to 1.
            In other words, the minimum value in the original range will take the value 0, 
            the maximum value will take 1 and the rest of the values in between the two 
            extremes will be appropriately scaled.

            Use Min-Max scaling (also known as normalization) when you want to scale the data to a specific range, typically between 0 and 1. This scaling technique preserves the relative relationships between the data points and is useful when you have a specific range requirement or when your data does not follow a normal distribution.


        2) Standardization/variance Scalling/Z-score normalization:
            All the datapoints are subtracted by their means and the result is divided by
            distribution's variance or standard deviation, to arrive at a distribution with
            a 0 mean and 1 variance.

            Use Standardization when you want to transform the data to have zero mean and unit variance. This scaling technique is useful when your data follows a normal distribution or when you want to mitigate the influence of outliers.

8. Feature Creation: 

        Create new features by combining or transforming existing ones. This can include engineering domain-specific features or deriving time-based features like day of the week, month, or year.

Again, it's important to note that the specific order may vary based on the dataset and problem at hand. Additionally, feature engineering is an iterative process, so you may need to revisit and adjust previous steps based on insights gained during later steps.