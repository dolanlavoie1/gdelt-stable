import pandas as pd
from datetime import date, datetime, timedelta
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO


def read_gdelt(
    start_date: str | date | datetime = "20150218",
    end_date: str | date | datetime = datetime.today(),
    keywords: list | str = None,
    negative_keywords: list | str = None,
    locations: list | str = None,
    negative_locations: list | str = None,
    themes: list | str = None,
    negative_themes: list | str = None,
    output_format: str = "dataframe",
    output_path: str = None,
):
    """
    Read GDELT data for a given date range and filter by keywords, locations, and themes.

    Args:
        start_date (str/date/datetime): The start date (inclusive) in ISO format (YYYY-MM-DD HH:MM:SS) as a string. Can also be a date or datetime object. Defaults to 2015-02-18.
        end_date (str/date/datetime): The end date (inclusive) in ISO format (YYYY-MM-DD HH:MM:SS) as a string. Can also be a date or datetime object. Defaults to the current date and time.
        keywords (list/str): Article will only be included if it contains at least one of the keywords.
        negative_keywords (list/str): Article will be excluded if it contains any of the keywords.
        locations (list/str): Article will only be included if it contains at least one of the locations. Location can be an abbreviation or full name.
        negative_locations (list/str): Article will be excluded if it contains any of the locations. Location can be an abbreviation or full name.
        themes (list/str): Article will only be included if it contains at least one of the themes.
        negative_themes (list/str): Article will be excluded if it contains any of the themes.
        output_format (str): The format of the output data. Can be 'dataframe' 'json' or 'csv'. Defaults to 'dataframe'.
        output_path (str): Saves the output data to the specified path if provided.

    Returns:
        The filtered GDELT data in the specified output format (dataframe, json, or csv). If output_path is provided, the data will be saved to that path.
    """

    if output_format not in ["dataframe", "json", "csv"]:
        raise ValueError("output_format must be one of 'dataframe', 'json', or 'csv'")
    if isinstance(start_date, str):
        try:
            start_date = datetime.fromisoformat(start_date)
        except ValueError:
            raise ValueError(
                "start_date must be in ISO format (YYYY-MM-DD HH:MM:SS) or a date/datetime object"
            )
    if isinstance(end_date, str):
        try:
            end_date = datetime.fromisoformat(end_date)
        except ValueError:
            raise ValueError(
                "end_date must be in ISO format (YYYY-MM-DD HH:MM:SS) or a date/datetime object"
            )
    if start_date > end_date:
        raise ValueError("start_date must be less than or equal to end_date")
    if start_date < datetime(2015, 2, 18):
        raise ValueError("start_date must be greater than or equal to 2015-02-18")
    if end_date > datetime.today():
        raise ValueError(
            "end_date must be less than or equal to the current date and time"
        )

    url_list = []

    for i in range((end_date - start_date).seconds // 900 + 1):
        url_list.append(
            f"http://data.gdeltproject.org/gdeltv2/{(start_date + timedelta(minutes=15 * i)).strftime('%Y%m%d%H%M%S')}.gkg.csv.zip"
        )

    for url in url_list:
        with urlopen(url) as response:
            with ZipFile(BytesIO(response.read())) as zip_file:
                with zip_file.open(zip_file.namelist()[0]) as f:
                    df = pd.read_csv(f, sep="\t", header=None)
                    print(df)


read_gdelt("2020-01-01 12:00", "2020-01-01 12:15")
