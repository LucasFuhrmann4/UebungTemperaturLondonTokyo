from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__series_Tokyo = QLineSeries()
        self.__series_Tokyo.setName("Tokyo")
        self.__series_Tokyo.setColor(QColor('lightblue'))

        dates = [
            QDateTime(2025, 1, 1, 0, 0, 0),
            QDateTime(2025, 2, 1, 0, 0, 0),
            QDateTime(2025, 3, 1, 0, 0, 0),
            QDateTime(2025, 4, 1, 0, 0, 0),
            QDateTime(2025, 5, 1, 0, 0, 0),
            QDateTime(2025, 6, 1, 0, 0, 0),
            QDateTime(2025, 7, 1, 0, 0, 0),
            QDateTime(2025, 8, 1, 0, 0, 0),
            QDateTime(2025, 9, 1, 0, 0, 0),
            QDateTime(2025, 10, 1, 0, 0, 0),
            QDateTime(2025, 11, 1, 0, 0, 0),
            QDateTime(2025, 12, 1, 0, 0, 0)
        ]

        self.__series_Tokyo.append(dates[0].toMSecsSinceEpoch(), 7)
        self.__series_Tokyo.append(dates[1].toMSecsSinceEpoch(), 6.9)
        self.__series_Tokyo.append(dates[2].toMSecsSinceEpoch(), 9.5)
        self.__series_Tokyo.append(dates[3].toMSecsSinceEpoch(), 14.5)
        self.__series_Tokyo.append(dates[4].toMSecsSinceEpoch(), 18.4)
        self.__series_Tokyo.append(dates[5].toMSecsSinceEpoch(), 21.5)
        self.__series_Tokyo.append(dates[6].toMSecsSinceEpoch(), 25.2)
        self.__series_Tokyo.append(dates[7].toMSecsSinceEpoch(), 26.5)
        self.__series_Tokyo.append(dates[8].toMSecsSinceEpoch(), 23.3)
        self.__series_Tokyo.append(dates[9].toMSecsSinceEpoch(), 18.3)
        self.__series_Tokyo.append(dates[10].toMSecsSinceEpoch(), 13.9)
        self.__series_Tokyo.append(dates[11].toMSecsSinceEpoch(), 9.6)

        self.__series_London = QLineSeries()
        self.__series_London.setName("London")
        self.__series_London.setColor(QColor(''))

        self.__series_London.append(dates[0].toMSecsSinceEpoch(), 3.9)
        self.__series_London.append(dates[1].toMSecsSinceEpoch(), 4.2)
        self.__series_London.append(dates[2].toMSecsSinceEpoch(), 5.7)
        self.__series_London.append(dates[3].toMSecsSinceEpoch(), 8.5)
        self.__series_London.append(dates[4].toMSecsSinceEpoch(), 11.9)
        self.__series_London.append(dates[5].toMSecsSinceEpoch(), 15.2)
        self.__series_London.append(dates[6].toMSecsSinceEpoch(), 17)
        self.__series_London.append(dates[7].toMSecsSinceEpoch(), 16.6)
        self.__series_London.append(dates[8].toMSecsSinceEpoch(), 14.2)
        self.__series_London.append(dates[9].toMSecsSinceEpoch(), 10.3)
        self.__series_London.append(dates[10].toMSecsSinceEpoch(), 6.6)
        self.__series_London.append(dates[11].toMSecsSinceEpoch(), 4.8)


        x_axis = QDateTimeAxis()
        x_axis.setFormat("dd.MM.yyyy")
        x_axis.setTickCount(12)

        y_axis = QValueAxis()
        y_axis.setRange(0, 30)
        y_axis.setTickCount(7)
        y_axis.setTitleText("Temperature (°C)")

        chart = QChart()
        chart.setTitle("Monatliche Durchschnittstemperatur")
        chart.addSeries(self.__series_Tokyo)
        chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)

        self.__series_Tokyo.attachAxis(x_axis)
        self.__series_Tokyo.attachAxis(y_axis)

        chart.addSeries(self.__series_London)

        self.__series_London.attachAxis(x_axis)
        self.__series_London.attachAxis(y_axis)

        self.setChart(chart)





