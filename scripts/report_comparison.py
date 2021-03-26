#!/usr/bin/env python3

import logging
from itertools import zip_longest
import argparse
import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

PARAMS = {
    'error_bad_lines': False,
    'sep': ',',
    'header':  0,
    'low_memory': False
}


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Testing: {func.__name__}...')
        result = func(*args, **kwargs)
        if result:
            logging.info(f'Testing {func.__name__} has finished with success')
        else:
            logging.error(f'Testing {func.__name__} has finished with error')
    return wrapper

# compare size


@logging_decorator
def test_count_of_values(dataframe_1, dataframe_2):
    size_df1 = dataframe_1.iloc[:, 1].size
    size_df2 = dataframe_2.iloc[:, 1].size
    if size_df1 == size_df2:
        return True
    return False

# compare both files


@logging_decorator
def test_entire_dataframe(dataframe_1, dataframe_2):
    return dataframe_1.equals(dataframe_2)

# compare columns are in order or not


@logging_decorator
def test_columns_order(dataframe_1, dataframe_2):
    for i in zip_longest(dataframe_1.columns, dataframe_2.columns):
        if i[0] != i[1]:
            return False
    else:
        return True

# if numeric fields compare sums


@logging_decorator
def test_sum_of_numeric_fields(dataframe_1, dataframe_2):
    features = list(dataframe_1.dtypes.where(
        lambda col_type: col_type == 'float64').dropna().index)
    for feature in features:
        ft_sum_df_1 = dataframe_1[feature].sum()
        ft_sum_df_2 = dataframe_2[feature].sum()
        if ft_sum_df_1 != ft_sum_df_2:
            logging.error(
                f'Error on {feature} - {ft_sum_df_1} != {ft_sum_df_2}')
            return False
    else:
        return True

# check headers of both files


def find_header_of_table(file_loc):
    with open(file_loc) as f:
        sensor_of_header = False
        for index, line in enumerate(f):
            if not line.strip():
                sensor_of_header = True
            elif sensor_of_header:
                row = index
                return row


def read_dataframe(file_loc, **kwargs):
    return pd.read_csv(file_loc, **kwargs)


def test_alternative_way_of_comparison(dataframe_1, dataframe_2):
    try:
        comaprison_df = dataframe_1 == dataframe_2
    except ValueError:
        logging.debug(
            'If you want to see debugging, make files to have the same amount of data')
        raise EnvironmentError('Rows count is not equal')

    for i in comaprison_df:
        not_equal_rows = comaprison_df[~comaprison_df[i]]

        if not_equal_rows.size:
            first_not_equal_row = not_equal_rows.index[0]
            logging.debug('\n' * 2)
            logging.error(f'Appeared for row {first_not_equal_row + 1}')
            logging.debug('-' * 100)
            logging.debug(
                f'''base file '{i}' column: {dataframe_1.loc[first_not_equal_row, i]}''')
            logging.debug(
                f'''to_compare file '{i}' column: {dataframe_2.loc[first_not_equal_row, i]}''')
            logging.debug('*' * 100)


def main(file_1, file_2):
    data_starts_at = find_header_of_table(file_1)

    PARAMS['header'] = data_starts_at - 2

    report_base_df = read_dataframe(file_1, **PARAMS)
    report_to_compare_df = read_dataframe(file_2, **PARAMS)

    test_columns_order(report_base_df, report_to_compare_df)
    test_count_of_values(report_base_df, report_to_compare_df)
    test_sum_of_numeric_fields(report_base_df, report_to_compare_df)
    result = test_entire_dataframe(report_base_df, report_to_compare_df)

    if not result:
        PARAMS['keep_default_na'] = False

        report_base_df = read_dataframe(file_1, **PARAMS)
        report_to_compare_df = read_dataframe(file_2, **PARAMS)
        test_alternative_way_of_comparison(
            report_base_df, report_to_compare_df)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Automated test for reports files'
    )

    parser.add_argument(
        '--file1',
        type=str,
        help='File which code treat like a role model',
        required=True,
    )

    parser.add_argument(
        '--file2',
        type=str,
        help='File which compare with role model',
        required=True,
    )

    args = parser.parse_args()
    main(args.file1, args.file2)
