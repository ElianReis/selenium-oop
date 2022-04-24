from src.robo import RoboPetro
from src.logger import logger
import glob
import os
import pandas as pd


class Tratamento:
    def __init__(self, countries):
        for country in countries:
            self.indicador = RoboPetro(country)
            try:
                self.cleaner(country)
            except Exception as e:
                logger.error("*** ERROR ***")
                logger.error(e, exc_info=True)
            self.indicador.browser.quit()

    def cleaner(self, indicator):
        list_of_files = glob.glob(self.indicador.path + "\\*")
        latest_file = max(list_of_files, key=os.path.getctime)
        logger.info("Realizando o tratamento de {}".format(latest_file.split('\\')[-1]))

        if indicator == "JAPAO CPI":
            df = pd.read_excel(
                latest_file,
                index_col=None,
                na_values=[""],
                usecols="H:I",
                skiprows=11,
                sheet_name=0,
            )
            df.drop(df.tail(8).index, inplace=True)
            df.drop(df.index[2:482], inplace=True)
            df.rename(columns={"Unnamed: 7": "Year/Month"}, inplace=True)
            self.save(df, indicator)

        elif indicator == 'JAPAO PPI':
            df = pd.read_csv(latest_file, sep=',', encoding='latin-1', skiprows=1, dtype=str, na_values='')
            df = df.dropna()
            self.save(df, indicator)

        elif indicator == 'AUSTRIA HICP':
            df = pd.read_csv(latest_file, sep=",", skiprows=range(1, 43), dtype=str)
            df = df.loc[
                df["indicator"] == "HICP15 - EU harmonised index of consumer prices, 2015=100"
                ]
            df = df[["month", "year", "values"]]
            df.reset_index(inplace=True, drop=True)
            m = {
                "Jan": "01",
                "Feb": "02",
                "Mar": "03",
                "Apr": "04",
                "May": "05",
                "Jun": "06",
                "Jul": "07",
                "Aug": "08",
                "Sep": "09",
                "Oct": "10",
                "Nov": "11",
                "Dec": "12",
            }
            for a, b in m.items():
                df["month"] = df["month"].str.replace(b, a, regex=False)
            df["year"] = df["year"].str.replace(r"(^.{1,2})", "", regex=True)
            df["Index 2015=100"] = df[["month", "year"]].agg(". ".join, axis=1)
            df["Overall index"] = df["values"]
            df.drop(["month", "year", "values"], axis=1, inplace=True)
            self.save(df, indicator)

        elif indicator == 'ALEMANHA CPI':
            df = pd.read_csv(latest_file, sep=";", encoding="latin-1", skiprows=6, dtype=str)
            df = df.drop(df.columns[[-1, -2]], axis=1)
            df.rename(
                columns={
                    "Unnamed: 0": "Year",
                    "Unnamed: 1": "Month",
                    "2015=100": "Verbraucherpreisindex 2015=100",
                },
                inplace=True,
            )
            df.drop(df.tail(3).index, inplace=True)
            df = df[~(df[["Verbraucherpreisindex 2015=100"]] == "...").any(axis=1)]
            self.save(df, indicator)

        elif indicator == "HOLANDA CPI":
            df = pd.read_csv(latest_file, sep=";", encoding="utf8", skiprows=range(1, 183))
            df.rename(columns={"2015 = 100": "CPI 2015=100"}, inplace=True)
            df = df.drop(df.columns[[-1]], axis=1)
            self.save(df, indicator)

        elif indicator == "HOLANDA PPI":
            df = pd.read_csv(latest_file, sep=";", encoding="utf8")
            self.save(df, indicator)

        else:
            logger.error("*** ERROR ***")
            logger.error('Nenhum indicador relacionado a {}'.format(indicator))

    @staticmethod
    def save(df, indicator):
        df.to_excel(
            os.getcwd() + "\\tratados\\" + indicator.upper() + "\\" + indicator + ".xls",
            sheet_name=indicator,
            index=False,
        )
        logger.info("Finalizado a coleta do indicador {}".format(indicator))
