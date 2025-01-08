import pandas as pd
import re


class Utilities:
    """
    Class of functions used to clean and prepare the data
    """
    def clean_amount(amount):
        '''Function to remove non-numeric characters except decimal points'''
        cleaned = re.sub(r'[^\d.]', '', str(amount))
        return cleaned
    
    def filter_rows_by_multiple_criteria(transactions, criteria):
    
        """
        Filters rows in a DataFrame based on multiple criteria. Returns rows that match any of the specified criteria.

        Parameters:
            transactions (pd.DataFrame): The input DataFrame to be filtered.
            criteria (dict): A dictionary where keys are column names and values are substrings (single string or list of strings).

        Returns:
            pd.DataFrame: A filtered DataFrame containing rows that match any of the specified criteria.
        """
        if not isinstance(criteria, dict):
            raise ValueError("Criteria must be provided as a dictionary with column names as keys and substrings as values.")

        # Initialize an empty filter (all False)
        combined_filter = pd.Series(False, index=transactions.index)

        # Loop through each column and corresponding substrings
        for column, substrings in criteria.items():
            if column not in transactions.columns:
                raise ValueError(f"Column '{column}' not found in the DataFrame.")

            # Handle single substring or list of substrings
            if isinstance(substrings, list):
                column_filter = transactions[column].apply(lambda x: any(sub in str(x) for sub in substrings))
            else:
                column_filter = transactions[column].str.contains(substrings, case=False, na=False)

            # Combine the current filter with the overall filter (logical OR)
            combined_filter |= column_filter

        # Apply the combined filter to the DataFrame
        return transactions[combined_filter]
    
    def extract_transaction_details_inplace(df, details_column='Details', start_phrases=None):
        """
        Extracts phone numbers and names from rows in the specified column that start with given phrases.
        Adds the extracted data as new columns to the original DataFrame.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            details_column (str): The name of the column containing the transaction details.
            start_phrases (list): A list of phrases to filter rows (e.g., ["Funds received from", "Customer Transfer to"]).

        Returns:
            pd.DataFrame: The updated DataFrame with new columns 'Phone Number' and 'Name'.
        """
        if details_column not in df.columns:
            raise ValueError(f"Column '{details_column}' not found in the DataFrame.")

        if not start_phrases or not isinstance(start_phrases, list):
            raise ValueError("start_phrases must be a list of starting phrases (e.g., ['Funds received from']).")

        for phrase in start_phrases:
            # Filter rows starting with the specific phrase
            filtered_rows = df[details_column].str.startswith(phrase, na=False)

            # Extract phone numbers (including masked numbers with asterisks)
            phone_numbers = df.loc[filtered_rows, details_column].str.extract(
                r'(07\*{2,}\d{3}|2547\*{2,}\d{3}|\+2547\*{2,}\d{3}|07\d{8}|254\d{9}|\+254\d{9})'
            )[0]
            df.loc[filtered_rows, 'Phone Number'] = phone_numbers

            # Extract names based on the phrase
            if phrase == "Funds received from":
                names = df.loc[filtered_rows, details_column].str.extract(
                    r'from\s-\s[\d\*\+]+\s([A-Za-z\s]+)'
                )[0]
            elif phrase == "Customer Transfer to":
                names = df.loc[filtered_rows, details_column].str.extract(
                    r'to\s-\s[\d\*\+]+\s([A-Za-z\s]+)'
                )[0]
            else:
                names = None

            # Assign extracted names to the DataFrame
            df.loc[filtered_rows, 'Name'] = names

        return df
    
    def filter_rows_by_characters(transactions, column_name, substring):
        '''Function to filter rows based on characters in a column'''
        filtered_df = transactions[transactions[column_name].str.contains(substring, case=False, na=False)]
        return filtered_df
    
   
    def extract_till_and_agent(df, details_col):
        """
        Extracts Till Number and Agent Name from the specified details column of a DataFrame
        and adds them as new columns.

        Parameters:
        df (pd.DataFrame): The input DataFrame.
        details_col (str): The column name containing details to extract information from.

        Returns:
        pd.DataFrame: The modified DataFrame with new columns 'Agent Till' and 'Agent Name'.
        """
        # Regex pattern to extract till number and all text after it
        pattern = r'Till\n(\d+)\s*-\s*(.*)'  # The (.*) captures everything after 'Till\n<digits> -'

        # Extracting till number and agent name
        extracted = df[details_col].str.extract(pattern)
        df['Agent Till'] = extracted[0]
        df['Agent Name'] = extracted[1]

        return df
    
