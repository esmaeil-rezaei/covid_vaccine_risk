# from src.exception_handler import handle_exception
# from src.logger import logging
# from src.utils import binary_encoder, date_feature_extractor


# def data_preprocessing(df):
#     """
#     Preprocess the DataFrame by dropping unnecessary columns.

#     This method drops the 'Heart Attack Date' column from the DataFrame.

#     Args:
#         df (pd.DataFrame): The input DataFrame to preprocess.

#     Returns:
#         pd.DataFrame: The preprocessed DataFrame.
#     """
#     try:
#         df = binary_encoder(
#             df, heart_attack_date="Heart Attack Date", target_column_name="target"
#         )
#         date_feature_extractor(df, date_column="Heart Attack Date")
#         date_feature_extractor(df, date_column="Vaccination Date")

#         return df
#     except Exception as e:
#         raise handle_exception(e)
