import flet as ft
import flet_charts as fch


data = {
    "dates": [

        "2026/03/01","2026/03/02","2026/03/03","2026/03/04","2026/03/05",
        "2026/03/06","2026/03/07","2026/03/08","2026/03/09","2026/03/10",
        "2026/03/11","2026/03/12","2026/03/13","2026/03/14","2026/03/15",
        "2026/03/16","2026/03/17","2026/03/18","2026/03/19","2026/03/20",
        "2026/03/21","2026/03/22","2026/03/23","2026/03/24","2026/03/25",
        "2026/03/26","2026/03/27","2026/03/28","2026/03/29","2026/03/30",
        "2026/03/31"
    ],

    "sales": [
        6, 15, 14, 18, 20,
        25, 30, 22, 19, 17,
        21, 23, 28, 35, 40,
        26, 24, 22, 27, 31,
        38, 29, 25, 23, 26,
        30, 34, 45, 50, 42,
        48
    ]
}


points = [fch.LineChartDataPoint(i, data["sales"][i]) for i in range(len(data["dates"])) ]

y_labels = [fch.ChartAxisLabel(value=data["sales"][i], label=ft.Text(f"{data['sales'][i]}", color=ft.Colors.PRIMARY) ) for i in range(len(data["sales"]))]
y_axis = fch.ChartAxis(title=ft.Text("Nombre de produits vendus", color=ft.Colors.PRIMARY, font_family="PoppinsSemiBold"), title_size=30, labels=y_labels)


x_labels = [fch.ChartAxisLabel(value=i, label=ft.Text(f"{data['dates'][i].split("/")[2]}", color=ft.Colors.PRIMARY) ) for i in range(len(data["dates"]))]
x_axis = fch.ChartAxis(title=ft.Text("Jours", color=ft.Colors.PRIMARY, font_family="PoppinsSemiBold"), labels=x_labels)

chart = fch.LineChart(
    
    expand=True,
    data_series=fch.LineChartData(points, curved=True, color=ft.Colors.SECONDARY),
    horizontal_grid_lines=fch.ChartGridLines(4, color=ft.Colors.GREY_100),
    vertical_grid_lines=fch.ChartGridLines(2, color=ft.Colors.GREY_100),
    left_axis=y_axis,
    bottom_axis=x_axis,
)   





def sales_chart():

    return ft.Container(

        ft.Column(
            [
                ft.Text("Evolution des ventes dans la période", font_family="PoppinsBold", color=ft.Colors.PRIMARY),
                ft.Divider(ft.Colors.PRIMARY),
                ft.Container(chart, expand=True, height=440)
            ],
          
        ),

        expand=3,
        bgcolor= ft.Colors.WHITE,
        padding=10,
        border_radius=5,
      
    )
